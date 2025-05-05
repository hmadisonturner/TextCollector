# TextCollector Metadata Strategy

This document outlines the comprehensive strategy for handling bibliographic and contextual metadata in TextCollector.

## Core Principles

- **Scholarly Fidelity**: Maintain academic rigor in citation and attribution
- **Progressive Enhancement**: Allow incremental metadata enrichment
- **Flexible Acquisition**: Support multiple metadata sources and formats
- **Query Relevance**: Leverage metadata to improve search quality
- **Open Standards**: Align with established scholarly metadata conventions

## Metadata Architecture

### Layered Metadata Model

1. **Bibliographic Layer**
   - Title, author(s), publication date, DOI/ISBN
   - Journal/publisher, volume, issue, pages
   - URL, access date, language
   - Citation key for reference management

2. **Content-Specific Layer**
   - Abstract/summary
   - Keywords and subject classifications
   - Document type (article, book, thesis, etc.)
   - License and copyright information

3. **System Layer**
   - Source file information
   - Processing parameters (chunk size, overlap)
   - Embedding model and version
   - Creation/modification timestamps
   - Collection and chunk identifiers

### Metadata Acquisition Strategies

1. **Document Extraction**
   - Parse frontmatter (YAML, JSON) in text files
   - Extract metadata from document headers
   - Detect and parse citation formatting within texts
   - Apply heuristic extraction for common patterns

2. **External Sources**
   - Import from BibTeX, CSL-JSON, RIS formats
   - Lookup via DOI/ISBN/PMID to external services
   - Integration with reference managers (Zotero, Mendeley)
   - Batch import of metadata files

3. **Manual Assignment**
   - CLI parameters for individual documents
   - Bulk assignment to document sets
   - Interactive prompting for missing fields
   - Default templates for different document types

4. **Inference Mechanisms**
   - Derive metadata from filenames and paths
   - Extract publication year from content
   - Identify author patterns from text
   - AI-assisted metadata extraction

## Search and Retrieval Enhancements

1. **Query Refinement**
   - Filter by author, date range, publication type
   - Prioritize recent or specific sources
   - Exclude sources based on metadata criteria
   - Boost relevance of authoritative sources

2. **Context Enrichment**
   - Include relevant bibliographic context in AI prompts
   - Format citations according to specified styles
   - Provide source quality indicators
   - Track citation chains across documents

3. **Result Presentation**
   - Grouped results by publication/source
   - Chronological organization options
   - Authority-based result ranking
   - Complete citation information in outputs

## Implementation Priorities

### Phase 1: Foundation
- Basic bibliographic fields in storage schema
- Manual metadata assignment via CLI
- Simple metadata display in results
- Filename/path metadata inference

### Phase 2: Enhancement
- BibTeX/CSL-JSON import capability
- Frontmatter extraction from documents
- Metadata filtering in queries
- Enhanced citation formatting in results

### Phase 3: Integration
- DOI/ISBN lookup services
- Reference manager connectivity
- AI-assisted metadata extraction
- Advanced metadata-aware relevance ranking

## Data Schema

```json
{
  "bibliographic": {
    "title": "Document title",
    "authors": ["Author 1", "Author 2"],
    "date": "2023-05-15",
    "publication": "Journal or Publisher",
    "doi": "10.xxxx/xxxxx",
    "citation_key": "smith2023title"
  },
  "content": {
    "type": "article",
    "keywords": ["keyword1", "keyword2"],
    "abstract": "Brief document summary",
    "language": "en"
  },
  "system": {
    "source": "filename.txt",
    "chunk_id": "filename_0",
    "created_at": "2023-05-20T14:30:00Z",
    "embedding_model": "all-MiniLM-L6-v2",
    "chunk_size": 1000,
    "chunk_overlap": 100
  }
}
```

## Standards Alignment

TextCollector's metadata strategy aligns with established scholarly standards:

- **Citation Styles**: Support for common formats (APA, MLA, Chicago, IEEE)
- **Identifiers**: Integration with DOI, ISBN, ORCID, and other persistent IDs
- **Interoperability**: Compatibility with BibTeX, CSL-JSON, and RIS formats
- **Schemas**: Alignment with Dublin Core, Schema.org, and Crossref metadata fields