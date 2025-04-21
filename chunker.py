def chunk_text(text, chunk_size=1000, chunk_overlap=100):
    """
    Split text into overlapping chunks of specified size.
    
    Args:
        text: Source text string to chunk
        chunk_size: Maximum chunk length
        chunk_overlap: Overlap between chunks
        
    Returns:
        List of text chunks
    """
    if not text:
        return []
    
    if not isinstance(chunk_size, int) or chunk_size <= 0:
        raise ValueError("Chunk size must be a positive integer.")
    if not isinstance(chunk_overlap, int) or chunk_overlap < 0:
        raise ValueError("Chunk overlap must be a non-negative integer.")
    if chunk_overlap >= chunk_size:
        raise ValueError("Chunk size must be larger than chunk overlap.")
        
    # Split into paragraphs first to avoid breaking mid-paragraph if possible
    paragraphs = text.split('\n\n')
    chunks = []
    current_chunk = ""
    
    for paragraph in paragraphs:
        # If adding this paragraph would exceed chunk size, save current chunk and start a new one
        if len(current_chunk) + len(paragraph) > chunk_size:
            if current_chunk:
                chunks.append(current_chunk)
            
            # Handle case where paragraph itself exceeds chunk size
            if len(paragraph) > chunk_size:
                # Further split paragraph into sentence-like units
                sentences = paragraph.replace('. ', '.\n').split('\n')
                current_chunk = ""
                
                for sentence in sentences:
                    if len(current_chunk) + len(sentence) > chunk_size:
                        if current_chunk:
                            chunks.append(current_chunk)
                        # If a single sentence is too long, just split it by size
                        if len(sentence) > chunk_size:
                            for i in range(0, len(sentence), chunk_size - chunk_overlap):
                                chunks.append(sentence[i:i + chunk_size])
                        else:
                            current_chunk = sentence
                    else:
                        if current_chunk:
                            current_chunk += " " + sentence
                        else:
                            current_chunk = sentence
            else:
                # Start new chunk with overlap from previous chunk if possible
                words = current_chunk.split()
                overlap_words = words[-min(len(words), int(chunk_overlap / 5)):]
                current_chunk = ' '.join(overlap_words) + "\n\n" + paragraph
        else:
            if current_chunk:
                current_chunk += "\n\n" + paragraph
            else:
                current_chunk = paragraph
    
    # Add the last chunk if it's not empty
    if current_chunk:
        chunks.append(current_chunk)
    
    return chunks