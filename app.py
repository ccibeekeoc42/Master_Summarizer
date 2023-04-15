import streamlit as st
import os
from youtube_page import render_youtube_page
from wikipedia_page import render_wikipedia_page
from pdf_page import render_pdf_page
from chat_page import render_chat_page


st.set_page_config(page_title="PDF Reader and YouTube Player",
                   layout="wide", initial_sidebar_state="expanded")

st.title("Master Summarizer")
api_key = st.sidebar.text_input("Secret Key: ", type='password')
os.environ['OPENAI_API_KEY'] = api_key

tab_names = ["YouTube", "Wikipedia", "PDF", "Chat"]
tab_choice = st.sidebar.radio("Choose a Tab", tab_names)

if api_key:
    if tab_choice == "YouTube": render_youtube_page(api_key)
    elif tab_choice == "Wikipedia": render_wikipedia_page(api_key)
    elif tab_choice == "PDF": render_pdf_page(api_key)
    elif tab_choice == "Chat": render_chat_page(api_key)
    else: st.write("Bad File")
else: st.error("No Secret Key Found!!")
