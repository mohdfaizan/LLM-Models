from dotenv import load_dotenv

# Loading all the environment variabes
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro-vision")
#load gemini model
def get_gemini(question, image):
    if input != "":
        response = model.generate_content([question, image])
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config(page_title = "Q and A Demo")
st.header("Gemini Application")
input= st.text_input("Input: ",key = "input")

# image upload option
# Create a file uploader widget
uploaded_file = st.file_uploader("Choose a file", type = ["jpeg","jpg","png"])

# Check if a file was uploaded
if uploaded_file is not None:
    # Read the file contents
    image = Image.open(uploaded_file)
    st.image(image, caption = "uploaded Image..",use_column_width = True)

submit = st.button("Tell me about the image..")

# when submit is clicked
if submit:
    
    response=get_gemini(input, image)
    st.subheader("The Response is")
    st.write(response)