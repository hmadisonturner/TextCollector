# TextCollector
Retrieval-Augmented Generation (RAG) command line tool

- Index text files
- Query them semantically
- Ask Claude or DeepSeek questions about your text collections

## Vision

TextCollector aims to be:

1. A **useful general-purpose tool** for semantic search and question answering across personal and research document collections
2. A **flexible test bed** for experimenting with different approaches to textual research and knowledge management
3. An **exemplar of AI-human collaboration** in both its development methodology and application capabilities

By combining these elements, TextCollector strives to advance how we interact with, organize, and extract knowledge from text.

## Installation

```bash
# Clone the repository
git clone https://github.com/hmadisonturner/TextCollector.git
cd TextCollector

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
# Index text files
python text_collector.py --index path/to/file1.txt path/to/file2.txt

# Query the index
python text_collector.py --query "your search query"

# Ask questions about your data
python text_collector.py --ask "search query" "your specific question"
```

## Command Line Options

```
usage: python  text_collector.py [-h] [--index TEXT_FILE [TEXT_FILE ...]] [--query QUERY]
                              [--collection_name COLLECTION_NAME] [--ask QUERY QUESTION]
                              [--persist_directory PERSIST_DIRECTORY] [--chunk_size CHUNK_SIZE]
                              [--chunk_overlap CHUNK_OVERLAP] [--num_results NUM_RESULTS]
                              [--embedding_model EMBEDDING_MODEL] [--model MODEL]
                              [--temperature TEMPERATURE]

Semantic search and question answering for your text collections.

options:
  -h, --help            show this help message and exit
  --index TEXT_FILE [TEXT_FILE ...]
                        Create the ChromaDB index from one or more TXT files.
  --query QUERY         Query the ChromaDB index with a text string.
  --collection_name COLLECTION_NAME
                        Name of the ChromaDB collection.
  --ask QUERY QUESTION  Search context with QUERY and ask QUESTION about it
  --persist_directory PERSIST_DIRECTORY
                        Directory to persist the ChromaDB database.
  --chunk_size CHUNK_SIZE
                        Size of text chunks for indexing.
  --chunk_overlap CHUNK_OVERLAP
                        Overlap between text chunks for indexing.
  --num_results NUM_RESULTS
                        Number of search results to return for a query.
  --embedding_model EMBEDDING_MODEL
                        Name of the sentence transformer model to use.
  --model MODEL         Model to use for answering questions (claude-* or deepseek-*)
  --temperature TEMPERATURE
                        Sampling temperature (0.0 to 1.0)
```

## Project Structure

The project has been modularized into the following components:

- `__main__.py`: Application entry point
- `cli.py`: Command line interface and argument parsing
- `core.py`: Core application logic for question answering
- `chromadb.py`: Database operations with ChromaDB
- `chunker.py`: Text chunking functionality
- `claude.py`: Claude API client
- `deepseek.py`: DeepSeek API client
- `file_io.py`: File operations

## Requirements

- Python 3.7+
- ChromaDB
- Sentence Transformers
- Anthropic API key (for Claude models)
- DeepSeek API key (for DeepSeek models)

## Environment Variables

- `ANTHROPIC_API_KEY`: Your Anthropic API key for Claude models
- `DEEPSEEK_API_KEY`: Your DeepSeek API key for DeepSeek models

## Development Approach

TextCollector uses a documentation-driven development workflow optimized for collaboration between human developers and AI coding assistants:

- **Documentation Structure**: The `/docs` directory contains specifications, architecture decisions, and implementation plans
- **Rational Product Flow**: Planning documents feed directly into development tasks with clear traceability
- **AI-Friendly Context**: Structured documentation provides AI assistants with comprehensive project understanding

This approach improves development consistency and facilitates effective collaboration regardless of whether tasks are performed by humans or AI agents.
