import asyncio
import time
from typing import Dict, Any
from src.api_client import OpenAIClient
from src.audio_processor import AudioProcessor

class ParallelPipeline:
    """Independent parallel pipelines for each modality"""
    
    def __init__(self):
        self.api_client = OpenAIClient()
        self.audio_processor = AudioProcessor()
    
    async def process_audio_parallel(self, audio_path: str) -> Dict[str, Any]:
        """Process audio independently"""
        start_time = time.time()
        transcribed_text, status = self.audio_processor.transcribe_audio(audio_path)
        latency = time.time() - start_time
        
        return {
            "transcribed_text": transcribed_text,
            "status": status,
            "latency": latency,
            "modality": "audio"
        }
    
    async def process_text_parallel(self, text: str) -> Dict[str, Any]:
        """Process text independently"""
        start_time = time.time()
        response = self.api_client.text_completion(text)
        latency = time.time() - start_time
        
        return {
            "response": response,
            "latency": latency,
            "modality": "text"
        }
    
    async def process_multiple_modalities(self, tasks: List[Dict]) -> List[Dict]:
        """Process multiple modalities in parallel"""
        results = []
        for task in tasks:
            if task['type'] == 'audio':
                result = await self.process_audio_parallel(task['input'])
            elif task['type'] == 'text':
                result = await self.process_text_parallel(task['input'])
            results.append(result)
        
        return results
