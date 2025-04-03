# TextCollector
Retrieval-Augmented Generation (RAG) command line tool

- Index text files

- Query them semantically

- Ask Claude or DeepSeek questions about your text collections

```
usage: text_collector.py [-h] [--index TEXT_FILE [TEXT_FILE ...]] [--query QUERY]
                         [--collection_name COLLECTION_NAME] [--ask QUERY QUESTION]
                         [--persist_directory PERSIST_DIRECTORY] [--chunk_size CHUNK_SIZE]
                         [--chunk_overlap CHUNK_OVERLAP] [--num_results NUM_RESULTS]
                         [--embedding_model EMBEDDING_MODEL] [--model MODEL]

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
```
