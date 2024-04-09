"""
DevTechBytes
https://www.youtube.com/@DevTechBytes
"""
from ollama import generate
from config import Config
from helpers.image_helper import get_image_bytes

system_prompt = Config.SYSTEM_PROMPT

def analyze_image_file(image_file, model, user_prompt):
    ...

# handles stream response back from LLM
def stream_parser(stream):
    ...