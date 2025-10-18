import time
from typing import Dict, Any
from src.api_client import OpenAIClient
from src.audio_processor import AudioProcessor

class SequentialPipeline:
    """Sequential modality processing: audio→text→chat"""
    
    def __init__(self):
        self.api_client = OpenAIClient()
        self.audio_processor = AudioProcessor()
        self.latency_log = []
    
    def process_audio_chat(self, audio_path: str, user_prompt: str = None) -> Dict[str, Any]:
        """Process: Audio → Text → AI Response"""
        start_time = time.time()
        
        # Step 1: Audio to text
        audio_start = time.time()
        transcribed_text, audio_status = self.audio_processor.transcribe_audio(audio_path)
        audio_latency = time.time() - audio_start
        
        if not transcribed_text:
            return {"error": audio_status, "latency": time.time() - start_time}
        
        # Step 2: AI response
        chat_start = time.time()
        if user_prompt:
            final_prompt = f"{user_prompt}\n\nContext: {transcribed_text}"
        else:
            final_prompt = transcribed_text
            
        ai_response = self.api_client.text_completion(final_prompt)
        chat_latency = time.time() - chat_start
        
        total_latency = time.time() - start_time
        
        self.latency_log.append(total_latency)
        
        return {
            "transcribed_text": transcribed_text,
            "ai_response": ai_response,
            "latency": {
                "total": total_latency,
                "audio_processing": audio_latency,
                "ai_chat": chat_latency
            },
            "architecture": "sequential"
        }
