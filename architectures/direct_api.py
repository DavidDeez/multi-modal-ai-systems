import time
from typing import Dict, Any
from src.api_client import OpenAIClient

class DirectAPI:
    """Direct API integration pattern"""
    
    def __init__(self):
        self.api_client = OpenAIClient()
    
    def process_text_direct(self, text: str) -> Dict[str, Any]:
        """Direct text processing"""
        start_time = time.time()
        response = self.api_client.text_completion(text)
        latency = time.time() - start_time
        
        return {
            "response": response,
            "latency": latency,
            "architecture": "direct_api"
        }
    
    def process_vision_direct(self, image_path: str) -> Dict[str, Any]:
        """Direct vision processing"""
        start_time = time.time()
        response = self.api_client.vision_completion(image_path)
        latency = time.time() - start_time
        
        return {
            "response": response,
            "latency": latency,
            "architecture": "direct_api_vision"
        }
    
    def process_audio_direct(self, audio_path: str) -> Dict[str, Any]:
        """Direct audio processing (transcribe only)"""
        from src.audio_processor import AudioProcessor
        audio_processor = AudioProcessor()
        
        start_time = time.time()
        transcribed_text, status = audio_processor.transcribe_audio(audio_path)
        latency = time.time() - start_time
        
        return {
            "transcribed_text": transcribed_text,
            "status": status,
            "latency": latency,
            "architecture": "direct_api_audio"
        }
