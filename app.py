import os
import streamlit as st
from youtube_page import render_youtube_page
from wikipedia_page import render_wikipedia_page
from pdf_page import render_pdf_page
from chat_page import render_chat_page
from profile_page import render_profile_page


st.set_page_config(page_title="PDF Reader and YouTube Player",
                   layout="wide", initial_sidebar_state="expanded")

st.title("Master Summarizer")
api_key = st.sidebar.text_input("Secret Key: ", type='password')
os.environ['OPENAI_API_KEY'] = api_key

tab_names = ["YouTube", "Wikipedia", "PDF", "Chat"]
tab_choice = st.sidebar.radio("Choose a Tab", tab_names)

if api_key:
    try:
        if tab_choice == "YouTube": render_youtube_page(api_key)
        elif tab_choice == "Wikipedia": render_wikipedia_page(api_key)
        elif tab_choice == "PDF": render_pdf_page(api_key)
        elif tab_choice == "Chat": render_chat_page(api_key)
        else: st.write("Bad File")
    except Exception as e:
        st.error(f"An error occurred. Please ensure valid SecreteKey and correct input fotmat.\n Here's the error: {e}")
else: 
    st.error("No Secret Key Found!! Contact the author to request one!")
    render_profile_page()
