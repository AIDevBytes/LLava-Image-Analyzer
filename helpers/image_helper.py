"""
DevTechBytes
https://www.youtube.com/@DevTechBytes
"""
import tempfile
from PIL import Image
from PIL import IptcImagePlugin
import streamlit as st

def read_file_content(file_name):
    # opens file to read
    with open(file_name, 'r') as file:

        file_contents = file.read()

        return file_contents
    
def create_temp_file(text_file):
    # create a local tempfile of file that was selected to be uploaded
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmp:
        tmp.write(text_file.getvalue())
        tmp_path = tmp.name  # Save the path where the tempfile has been written

        return tmp_path
