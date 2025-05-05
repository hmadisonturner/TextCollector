# TextCollector Metadata Implementation Roadmap

This document outlines the phased implementation approach for adding bibliographic metadata capabilities to TextCollector.

## Phase 1: Foundation (Core Functionality)

**Timeline: 2-3 weeks**

### Tasks

1. **Base Schema Design**
   - Define core bibliographic fields
   - Implement backward compatibility layer
   - Create metadata validation utilities

2. **Storage Layer Updates**
   - Extend ChromaDB metadata structure
   - Add metadata indexing capabilities
   - Implement query filtering by metadata

3. **Basic Input Methods**
   - CLI parameters for manual metadata assignment
   - Simple frontmatter parsing (YAML/JSON)
   - Path/filename-based metadata inference

4. **Output Enhancements**
   - Display bibliographic information in search results
   - Include basic citation information in AI prompts
   - Simple metadata-only listing command

### Deliverables
- Updated schema in ChromaDB integration
- Enhanced CLI with basic metadata flags
- Documentation for metadata input formats
- Tests for core metadata functionality

## Phase 2: Enhancement (Advanced Features)

**Timeline: 3-4 weeks after Phase 1**

### Tasks

1. **External Format Support**
   - BibTeX import/export functionality
   - CSL-JSON compatibility
   - Bulk metadata assignment

2. **Content Extraction**
   - Enhanced frontmatter parsing
   - Title and author extraction heuristics
   - Keywords and abstract detection

3. **Query Improvements**
   - Metadata-based filtering commands
   - Time-based result organization
   - Author and source-based grouping

4. **Presentation Refinements**
   - Configurable citation styles
   - Rich metadata display in panels
   - Sorting options based on metadata fields

### Deliverables
- Import/export utilities for standard formats
- Advanced metadata extraction capabilities
- Enhanced query filters and presentation
- Integration tests for metadata workflows

## Phase 3: Integration (External Systems)

**Timeline: 4-6 weeks after Phase 2**

### Tasks

1. **External Services**
   - DOI resolution and metadata lookup
   - ISBN database integration
   - CrossRef/PubMed API connectivity

2. **Reference Management**
   - Zotero integration
   - Mendeley connectivity
   - BibTeX library synchronization

3. **AI Augmentation**
   - AI-assisted metadata extraction
   - Smart citation formatting
   - Automatic keyword generation

4. **Advanced Analytics**
   - Citation network visualization
   - Author collaboration graphs
   - Topic clustering by metadata

### Deliverables
- External service connectors
- Reference manager plugins/integrations
- AI enhancement utilities
- Metadata visualization tools

## Technical Implementation Details

### Schema Extensions

```python
# Extended metadata structure
metadata = {
    # Bibliographic layer
    "title": str,
    "authors": List[str],
    "date": str,  # ISO format: YYYY-MM-DD
    "publication": str,
    "doi": str,
    "citation_key": str,
    
    # Content layer
    "type": str,  # article, book, thesis, etc.
    "keywords": List[str],
    "abstract": str,
    "language": str,
    
    # System layer (existing + new)
    "source": str,  # Existing field
    "created_at": str,  # ISO timestamp
    "chunk_id": str,
    "embedding_model": str,
    "chunk_size": int,
    "chunk_overlap": int
}
```

### CLI Extensions

```
# Phase 1 CLI additions
--metadata KEY=VALUE        Add metadata field (can be used multiple times)
--metadata-file FILE        Import metadata from JSON/YAML file
--extract-metadata          Try to extract metadata from document content
--infer-metadata            Infer metadata from filename/path

# Phase 2 CLI additions
--bibtex FILE               Import metadata from BibTeX file
--csl-json FILE             Import metadata from CSL-JSON file
--citation-style STYLE      Format citations using specified style
--filter-metadata KEY=VALUE Filter results by metadata value
```

### API Extensions

```python
# Phase 1 API additions
def create_chroma_index(text_files, collection_name="text_collection",
                        chunk_size=1000, chunk_overlap=100,
                        embedding_model_name='all-MiniLM-L6-v2',
                        db_directory="chroma_db",
                        metadata=None, extract_metadata=False,
                        infer_metadata=False):
    # Implementation with metadata support
    
# Phase 2 API additions
def import_metadata(source_file, format="json"):
    # Import metadata from external files
    
def query_with_metadata_filter(query, metadata_filters=None):
    # Query with metadata filtering
```

## Dependencies and Requirements

### New Dependencies

- **Phase 1**:
  - PyYAML (for frontmatter parsing)
  - jsonschema (for metadata validation)

- **Phase 2**:
  - pybtex (for BibTeX handling)
  - citeproc-py (for citation formatting)

- **Phase 3**:
  - habanero (for DOI resolution)
  - pyzotero (for Zotero integration)

### Testing Requirements

- Unit tests for metadata parsing
- Integration tests for full document workflows
- Test fixtures for various metadata formats
- Performance testing for large metadata collections

## Risk Assessment and Mitigation

| Risk | Impact | Probability | Mitigation |
|------|--------|------------|------------|
| Schema compatibility issues | High | Medium | Careful version management, migration utilities |
| Performance degradation | Medium | Low | Indexing optimization, lazy loading of extended metadata |
| External API dependencies | Medium | Medium | Failover mechanisms, caching, offline capability |
| Complex extraction failures | Low | High | Fallback to manual entry, clear error reporting |

## Success Metrics

- **Coverage**: Percentage of documents with complete metadata
- **Accuracy**: Correctness of extracted/inferred metadata
- **Efficiency**: Time required for metadata operations
- **Adoption**: User engagement with metadata features
- **Query Enhancement**: Improvement in search relevance

## Maintenance Plan

- Regular schema validation against external standards
- Monitoring of external API changes
- Periodic updating of extraction heuristics
- User feedback collection for feature refinement