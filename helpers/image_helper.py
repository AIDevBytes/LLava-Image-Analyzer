"""
DevTechBytes
https://www.youtube.com/@DevTechBytes
"""
import io
import tempfile
from PIL import Image
    
def create_temp_file(text_file):
    # create a local tempfile of file that was selected to be uploaded
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmp:
        tmp.write(text_file.getvalue())
        tmp_path = tmp.name  # Save the path where the tempfile has been written

        return tmp_path

def get_image_bytes(image_file):
    # Open the image file
    image_path = image_file  # Replace with the path to your image file
    image = Image.open(image_path)

    # Convert the image to bytes
    with io.BytesIO() as output:
        image.save(output, format="png")  # Change the format as needed (e.g., JPEG, PNG)
        image_bytes = output.getvalue()
    
    return image_bytes