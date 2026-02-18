from typing import Dict, Any
import logging
from transformers import pipeline

class ContentGenerator:
    def __init__(self):
        self.image_gen = pipeline("image-generation", model="stability-ai/sdxl")
        self.text_gen = pipeline("text-generation", model="gpt2")

    def generate_image(self, prompt: str) -> Dict[str, Any]:
        """Generate an image from a text prompt."""
        try:
            result = self.image_gen(prompt)
            logging.info(f"Image generation successful with prompt: {prompt}")
            return {"status": "success", "data": result}
        except Exception as e:
            logging.error(f"Image generation failed: {str(e)}")
            return {"status": "error", "error": str(e)}

    def generate_text(self, prompt: str) -> Dict[str, Any]:
        """Generate text content from a prompt."""
        try:
            result = self.text_gen(prompt)
            logging.info(f"Text generation successful with prompt: {prompt}")
            return {"status": "success", "data": result}
        except Exception as e:
            logging.error(f"Text generation failed: {str(e)}")
            return {"status": "error", "error": str(e)}