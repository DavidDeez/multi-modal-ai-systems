import os
import gradio as gr
from src.api_client import OpenAIClient
from architectures.sequential_pipeline import SequentialPipeline
from architectures.direct_api import DirectAPI
from src.audio_processor import AudioProcessor
from src.text_processor import TextProcessor

# Initialize components - NO API KEY HERE
api_client = OpenAIClient()
sequential_pipeline = SequentialPipeline()
direct_api = DirectAPI()
audio_processor = AudioProcessor()
text_processor = TextProcessor()

# ... rest of your app.py code remains the same ...
