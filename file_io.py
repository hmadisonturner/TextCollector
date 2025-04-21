import os

def extract_text_from_txt(file_path):
    """
    Extract text content from a TXT file.
    
    Args:
        file_path: Path to the TXT file
        
    Returns:
        String containing the text content
    """
    text = ""
    try:
        with open(file_path, 'r', encoding='utf-8') as txt_file:
            text = txt_file.read()
    except Exception as e:
        print(f"Error reading TXT file {file_path}: {e}")
    return text