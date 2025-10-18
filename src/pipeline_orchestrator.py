from typing import Dict, Any
from src.api_client import OpenAIClient
from src.audio_processor import AudioProcessor
from src.text_processor import TextProcessor

class PipelineOrchestrator:
    """Orchestrates multi-modal processing pipelines"""
    
    def __init__(self):
        self.api_client = OpenAIClient()
        self.audio_processor = AudioProcessor()
        self.text_processor = TextProcessor()
    
    def orchestrate_sequential(self, audio_path: str, user_prompt: str = None) -> Dict[str, Any]:
        """Orchestrate sequential audio→text→chat pipeline"""
        # Audio to text
        transcribed_text, status = self.audio_processor.transcribe_audio(audio_path)
        if not transcribed_text:
            return {"error": status}
        
        # AI response
        if user_prompt:
            final_prompt = f"{user_prompt}\n\nContext: {transcribed_text}"
        else:
            final_prompt = transcribed_text
            
        ai_response = self.api_client.text_completion(final_prompt)
        
        return {
            "transcribed_text": transcribed_text,
            "ai_response": ai_response,
            "pipeline": "sequential"
        }
