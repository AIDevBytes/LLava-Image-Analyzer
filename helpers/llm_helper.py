"""
Orignal Author: DevTechBytes
https://www.youtube.com/@DevTechBytes
"""
import io
from ollama import generate
from PIL import Image
from config import Config

system_prompt = Config.SYSTEM_PROMPT

def analyze_image_file(image_file, model, user_prompt):
    # Open the image file
    image_path = image_file  # Replace with the path to your image file
    image = Image.open(image_path)

    # Convert the image to bytes
    with io.BytesIO() as output:
        image.save(output, format="png")  # Change the format as needed (e.g., JPEG, PNG)
        image_bytes = output.getvalue()

    stream = generate(model=model, 
            prompt=user_prompt, 
            images=[image_bytes], 
            stream=True)

    return stream

# handles stream response back from LLM
def stream_parser(stream):
    for chunk in stream:
        yield chunk['response']