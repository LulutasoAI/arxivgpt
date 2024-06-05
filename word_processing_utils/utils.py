
class WordProcessing:

    def __init__(self) -> None:
        pass
    
    def chunk_text(self, text, chunk_size):
        """Split a long text into chunks of a specified size."""
        chunks = []
        for i in range(0, len(text), chunk_size):
            chunk = text[i:i + chunk_size]
            chunks.append(chunk)
        return chunks
