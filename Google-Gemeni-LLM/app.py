from dotenv import load_dotenv

# Loading all the environment variabes
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")
#load gemini model
def get_gemini(question):
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title = "Q and A Demo")
st.header("Gemini Application")
input= st.text_input("Input: ",key = "input")
submit = st.button("Ask the Question")

# when submit is clicked
if submit:
    
    response=get_gemini(input)
    st.subheader("The Response is")
    st.write(response)