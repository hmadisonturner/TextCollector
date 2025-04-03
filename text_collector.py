import anthropic
import argparse
import chromadb
from deepseek import DeepSeekAPI
import os
from rich.console import Console
from rich.markdown import Markdown
from sentence_transformers import SentenceTransformer


def extract_text_from_txt(txt_path):
    """Extracts text content from a TXT file."""
    text = ""
    try:
        with open(txt_path, 'r', encoding='utf-8') as txt_file:
            text = txt_file.read()
    except Exception as e:
        print(f"Error reading TXT file {txt_path}: {e}")
    return text


def chunk_text(text, chunk_size=1000, chunk_overlap=100):
    """Splits text into smaller chunks with optional overlap."""
    if not isinstance(chunk_size, int) or chunk_size <= 0:
        raise ValueError("Chunk size must be a positive integer.")
    if not isinstance(chunk_overlap, int) or chunk_overlap < 0:
        raise ValueError("Chunk overlap must be a non-negative integer.")
    if chunk_overlap >= chunk_size:
        raise ValueError("Chunk size must be larger than chunk overlap.")
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        if end > len(text):
            end = len(text)
            chunk_overlap = 0
        chunks.append(text[start:end])
        start = end - chunk_overlap
    return chunks


def create_chroma_index(text_files,
                        collection_name="text_collection",
                        chunk_size=1000,
                        chunk_overlap=100,
                        embedding_model_name='all-MiniLM-L6-v2',
                        persist_directory="chroma_db"):
    """Creates a ChromaDB index from TXT files."""
    num_chunks = 0
    all_chunks = []
    metadatas = []
    ids = []

    model = SentenceTransformer(embedding_model_name)
    client = chromadb.PersistentClient(path=persist_directory)
    collection = client.get_or_create_collection(name=collection_name)

    for text_file in text_files:
        print(f"Processing: {text_file}")
        text = extract_text_from_txt(text_file)
        chunks = chunk_text(text, chunk_size, chunk_overlap)
        all_chunks.extend(chunks)
        metadatas.extend(
            [{"source": os.path.basename(text_file)}] * len(chunks))
        ids.extend(
            [f"{os.path.basename(text_file)}_{i}" for i in range(len(chunks))])
        num_chunks += len(chunks)

    if not all_chunks:
        print("No text extracted from the provided TXT files.")
        return

    print(f"Chunks: {num_chunks}")
    embeddings = model.encode(all_chunks)
    collection.add(
        embeddings=embeddings.tolist(),
        documents=all_chunks,
        metadatas=metadatas,
        ids=ids
    )

    print(
        f"ChromaDB index created and saved to {persist_directory} with "
        f"collection name '{collection_name}'")


def query_chroma_index(query,
                       collection_name="text_collection",
                       num_results=5,
                       embedding_model_name='all-MiniLM-L6-v2',
                       persist_directory="chroma_db",
                       return_results=False):
    """Queries the ChromaDB index and optionally returns results."""
    client = chromadb.PersistentClient(path=persist_directory)
    try:
        collection = client.get_collection(name=collection_name)
    except BaseException:
        print(
            f"Collection '{collection_name}' not found in {persist_directory}"
            ". Please create the index first using the --index option."
        )
        return None

    model = SentenceTransformer(embedding_model_name)
    query_embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=num_results
    )

    print(f"\nQuery: {query}\n")
    if results and results['documents'] and results['metadatas']:
        for i in range(len(results['documents'][0])):
            print(f"Result {i+1}:")
            print(f"  File: {results['metadatas'][0][i]['source']}")
            print(f"  Content: {results['documents'][0][i]}")
            print(f"  Distance: {results['distances'][0][i]:.4f}")
            print("-" * 20)

        if return_results:
            return results
    else:
        print("No matching results found.")
        return None


def format_qa_prompt(query, results, prompt_template=None):
    """
    Format query results into a QA prompt.

    Args:
        query: The user's question
        results: ChromaDB query results
        prompt_template: Optional custom template. If None, uses default format.

    Returns:
        Formatted prompt string for QA model
    """
    if not results or not results['documents'] or not results['metadatas']:
        return None

    if prompt_template is None:
        prompt_template = (
            "Context information is below.\n"
            "---------------------\n"
            "{context}\n"
            "---------------------\n"
            "Given the context information and not prior knowledge, answer the question:\n"
            "Question: {question}\n"
            "Answer:"
        )

    context_parts = []
    for i in range(len(results['documents'][0])):
        metadata = results['metadatas'][0][i]
        source = metadata['source']
        content = results['documents'][0][i]

        context_parts.append(
            f"[Source: {source}]\n{content}"
        )

    context = "\n\n".join(context_parts)
    prompt = prompt_template.format(context=context, question=query)

    return prompt


def query_deepseek(prompt, model="deepseek-chat", temperature=0.7):
    """
    Query DeepSeek API with a prompt and return the response.

    Args:
        prompt: The formatted prompt string
        model: DeepSeek model to use
        temperature: Sampling temperature (0.0 to 1.0)

    Returns:
        Response text from DeepSeek
    """
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError(
            "DEEPSEEK_API_KEY environment variable not set. "
            "Please set your API key first."
        )

    try:
        client = DeepSeekAPI(api_key)
        response = client.chat_completion(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error querying DeepSeek API: {str(e)}")
        return None # Or a more informative error message


def query_claude(prompt, model="claude-3-opus-20240229", temperature=0.7):
    """
    Query Claude API with a prompt and return the response.

    Args:
        prompt: The formatted prompt string
        model: Claude model to use
        temperature: Sampling temperature (0.0 to 1.0)

    Returns:
        Response text from Claude
    """
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError(
            "ANTHROPIC_API_KEY environment variable not set. "
            "Please set your API key first."
        )

    try:
        client = anthropic.Anthropic(api_key=api_key)
        response = client.messages.create(
            max_tokens=2048,
            model=model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text
    except Exception as e:
        return f"Error querying Claude API: {str(e)}"


def display_markdown_response(response):
    """Display the response text as formatted markdown."""
    console = Console()
    md = Markdown(response)
    console.print(md)


def answer_question(search_query, question, collection_name="text_collection",
                    num_results=5, model="deepseek-chat"):
    """
    End-to-end pipeline to answer questions using retrieved context.

    Args:
        query: Search query for finding relevant context
        question: The specific question to answer
        collection_name: Name of the ChromaDB collection
        num_results: Number of context chunks to retrieve
        model: DeepSeek model to use
    """
    # Get relevant chunks
    results = query_chroma_index(search_query, collection_name=collection_name,
                                 num_results=num_results, return_results=True)
    if not results:
        print("No relevant context found to answer the question.")
        return

    # Format prompt with context and question
    prompt = format_qa_prompt(question, results)

    # Get answer based on model type
    if model.startswith("deepseek"):
        response = query_deepseek(prompt, model=model)
    else:
        response = query_claude(prompt, model=model)

    # Display formatted response
    print("\nAnswer:")
    print("-------")
    display_markdown_response(response)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create and query a ChromaDB vector store from text files."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--index",
        nargs='+',
        help="Create the ChromaDB index from one or more TXT files."
    )
    group.add_argument(
        "--query",
        type=str,
        help="Query the ChromaDB index with a text string."
    )
    parser.add_argument(
        "--collection_name",
        type=str,
        default="text_collection",
        help="Name of the ChromaDB collection."
    )
    group.add_argument(
        "--ask",
        nargs=2,
        metavar=('QUERY', 'QUESTION'),
        help="Search context with QUERY and ask QUESTION about it"
    )
    parser.add_argument(
        "--persist_directory",
        type=str,
        default="chroma_db",
        help="Directory to persist the ChromaDB database."
    )
    parser.add_argument(
        "--chunk_size",
        type=int,
        default=1000,
        help="Size of text chunks for indexing."
    )
    parser.add_argument(
        "--chunk_overlap",
        type=int,
        default=100,
        help="Overlap between text chunks for indexing."
    )
    parser.add_argument(
        "--num_results",
        type=int,
        default=5,
        help="Number of search results to return for a query."
    )
    parser.add_argument(
        "--embedding_model",
        type=str,
        default='all-MiniLM-L6-v2',
        help="Name of the sentence transformer model to use."
    )
    parser.add_argument(
        "--model",
        type=str,
        default="claude-3-opus-20240229",
        help="DeepSeek model to use for answering questions"
    )

    args = parser.parse_args()

    if args.index:
        create_chroma_index(
            args.index,
            args.collection_name,
            args.chunk_size,
            args.chunk_overlap,
            args.embedding_model,
            args.persist_directory
        )
    elif args.query:
        query_chroma_index(
            args.query,
            args.collection_name,
            args.num_results,
            args.embedding_model,
            args.persist_directory
        )
    elif args.ask:
        answer_question(
            search_query=args.ask[0],
            question=args.ask[1],
            collection_name=args.collection_name,
            num_results=args.num_results,
            model=args.model
        )
