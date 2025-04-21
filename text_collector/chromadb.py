from text_collector.chunker import chunk_text
from text_collector.file_io import extract_text_from_txt
import chromadb
import os
from sentence_transformers import SentenceTransformer


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
    except chromadb.errors.InvalidCollectionName:
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
