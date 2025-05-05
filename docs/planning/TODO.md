# TextCollector Bibliographic Metadata Implementation Plan

## Core Library Changes

### 1. Extend Metadata Structure in ChromaDB
- Add standard bibliographic fields (title, author, date, publisher, etc.)
- Update collection schema to support extended metadata
- Ensure backward compatibility with existing documents
- Implement metadata filtering/querying capabilities

### 2. Update File I/O Layer
- Create metadata extraction functions for different file formats
- Support frontmatter/YAML metadata in text files
- Add functions to parse bibliographic metadata from filenames
- Support external metadata sources (e.g., BibTeX, CSL-JSON)

### 3. Update Core Processing
- Enhance format_qa_prompt() to include relevant metadata in context
- Add metadata-aware sorting/filtering of search results
- Implement metadata validation functions
- Support citation formatting in different styles

## CLI Enhancements

### 1. Command Line Interface Updates
- Add metadata-related arguments to index command:
  - `--metadata-file` for JSON/YAML file with metadata
  - `--metadata` for inline key=value pairs
  - `--extract-metadata` flag to extract from content
- Support bulk metadata assignment to multiple files

### 2. Output Formatting
- Update Rich panels to display bibliographic information
- Add citation formatting options
- Implement metadata-only view for indexed documents
- Support export of metadata in standard formats

## Future Extensions
- Integration with reference management systems (Zotero, Mendeley)
- DOI/ISBN lookup for automatic metadata population
- Full-text citation detection and cross-referencing
- Custom metadata schemas for different document types