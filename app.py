import streamlit as st
from transformers import pipeline

# Load sentiment analysis pipeline
pipe = pipeline('sentiment-analysis')

# Create a text area for user input
text = st.text_area('Enter some text')

# If text is provided, perform sentiment analysis and display the result
if text:
    result = pipe(text)
    st.json(result)
