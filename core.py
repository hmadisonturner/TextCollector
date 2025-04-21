import os
from TextCollector.chromadb import query_chroma_index
from TextCollector.claude import query_claude
from TextCollector.deepseek import query_deepseek

def format_qa_prompt(question, results, prompt_template=None):
    """
    Format query results into a QA prompt.

    Args:
        question: The user's question
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
    prompt = prompt_template.format(context=context, question=question)

    return prompt

def answer_question(search_query, question, collection_name="text_collection",
                    num_results=5, model="deepseek-chat", temperature=0.7):
    """
    End-to-end pipeline to answer questions using retrieved context.

    Args:
        query: Search query for finding relevant context
        question: The specific question to answer
        collection_name: Name of the ChromaDB collection
        num_results: Number of context chunks to retrieve
        model: DeepSeek model to use
        temperature: Sampling temperature (0.0 to 1.0)
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
        api_key = os.getenv("DEEPSEEK_API_KEY")
        if not api_key:
            raise ValueError(
                "DEEPSEEK_API_KEY environment variable not set. "
                "Please set your API key first."
            )

        response = query_deepseek(prompt, model, api_key)
    else:
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError(
                "ANTHROPIC_API_KEY environment variable not set. "
                "Please set your API key first."
            )

        response = query_claude(prompt, api_key, model=model, temperature=temperature)

    return response