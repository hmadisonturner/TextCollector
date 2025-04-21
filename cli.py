from TextCollector.core import answer_question
from TextCollector.chromadb import create_chroma_index, query_chroma_index
import argparse
from rich.console import Console
from rich.markdown import Markdown


def display_markdown_response(response):
    """Display the response text as formatted markdown."""
    console = Console()
    md = Markdown(response)
    console.print(md)

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Semantic search and question answering for your text collections."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--index",
        nargs='+',
        metavar="TEXT_FILE",
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
        help="Model to use for answering questions (claude-* or deepseek-*)"
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.7,
        help="Sampling temperature (0.0 to 1.0)"
    )

    return parser.parse_args()

def main():
    """Entry point for CLI execution."""
    args = parse_args()
    try:
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
            response = answer_question(
                search_query=args.ask[0],
                question=args.ask[1],
                collection_name=args.collection_name,
                num_results=args.num_results,
                model=args.model,
                temperature=args.temperature
            )
            if response:
                print("\nAnswer:")
                print("-------")
                display_markdown_response(response)
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1