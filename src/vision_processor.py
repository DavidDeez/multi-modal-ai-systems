from src.api_client import OpenAIClient

class VisionProcessor:
    def __init__(self):
        self.api_client = OpenAIClient()
    
    def describe_image(self, image_path: str) -> str:
        """Process image description using vision API"""
        return self.api_client.vision_completion(image_path)
