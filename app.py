import streamlit as st
from config import Config
from helpers.image_helper import create_temp_file
from helpers.llm_helper import analyze_image_file, stream_parser

page_title = Config.PAGE_TITLE

# configures page settings
st.set_page_config(
    page_title=page_title,
    initial_sidebar_state="expanded",
)

# page title
st.title(page_title)

st.markdown("#### Select an image file to analyze.")

# displays file upload widget
uploaded_file = st.file_uploader("Choose image file", type=['png', 'jpg', 'jpeg'] )

# sets up sidebar nav widgets
with st.sidebar:   
    # creates selectbox to pick the model we would like to use
    image_model = st.selectbox('Which image model would you like to use?', Config.OLLAMA_MODELS)

if chat_input := st.chat_input("What would you like to ask?"):
    if uploaded_file is None:
        st.error('You must select an image file to analyze!')
        st.stop()

    # Color formatting example https://docs.streamlit.io/library/api-reference/text/st.markdown
    with st.status(":red[Processing image file. DON'T LEAVE THIS PAGE WHILE IMAGE FILE IS BEING ANALYZED...]", expanded=True) as status:
        st.write(":orange[Analyzing Image File...]")

        # creates the audio file
        stream = analyze_image_file(uploaded_file, model=image_model, user_prompt=chat_input)
       
        stream_output = st.write_stream(stream_parser(stream))

        st.write(":green[Done analyzing image file]")
