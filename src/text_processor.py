class TextProcessor:
    @staticmethod
    def summarize_text(text: str, max_length: int = 10000) -> str:
        """Prepare text for summarization with length limits"""
        if not text.strip():
            return "Empty text provided"
        
        if len(text) > max_length:
            text = text[:max_length] + "... (truncated)"
        
        return text
    
    @staticmethod
    def extract_file_content(file_path: str) -> str:
        """Extract text content from various file types"""
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                return f.read()
        except Exception as e:
            return f"File reading error: {str(e)}"
