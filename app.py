import os
import gradio as gr
from src.api_client import OpenAIClient
from architectures.sequential_pipeline import SequentialPipeline
from architectures.direct_api import DirectAPI

# Initialize components lazily
api_client = OpenAIClient()
sequential_pipeline = SequentialPipeline()
direct_api = DirectAPI()

def process_text(api_key, text_input):
    os.environ["OPENAI_API_KEY"] = api_key
    return api_client.text_completion(prompt=text_input)

with gr.Blocks() as demo:
    gr.Markdown("# Multi-Modal AI System (OpenRouter Edition)")
    
    api_key_input = gr.Textbox(
        label="OpenRouter API Key", 
        placeholder="sk-or-v1-...", 
        type="password"
    )
    
    with gr.Tab("Text Completion"):
        with gr.Row():
            with gr.Column():
                text_in = gr.Textbox(label="Input Text")
                submit_btn = gr.Button("Submit")
            with gr.Column():
                text_out = gr.Textbox(label="AI Response")
                
        submit_btn.click(
            fn=process_text, 
            inputs=[api_key_input, text_in], 
            outputs=text_out
        )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    demo.launch(server_name="0.0.0.0", server_port=port)
