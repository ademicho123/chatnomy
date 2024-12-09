import streamlit as st
import os
from dotenv import load_dotenv
from utils import handle_file_upload, query_together_api

# Load environment variables
load_dotenv()

TOGETHER_AI_API_KEY = os.getenv("TOGETHER_AI_API_KEY")
TOGETHER_AI_API_URL = os.getenv("TOGETHER_AI_API_URL")

# Streamlit App
st.title("UniChat AI - Your AI File Assistant")
st.sidebar.header("Upload Files")
uploaded_files = st.sidebar.file_uploader("Upload files", accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        st.write(f"**Uploaded File:** {file.name}")
        file_content = handle_file_upload(file)
        st.text_area(f"Content of {file.name}", value=file_content, height=200)
        if st.button(f"Query AI about {file.name}"):
            response = query_together_api(TOGETHER_AI_API_KEY, TOGETHER_AI_API_URL, file_content)
            st.write(f"**Response:** {response}")
else:
    st.write("Upload any file to begin.")

st.write("---")
st.write("Powered by [Together AI](https://together.xyz/)")
