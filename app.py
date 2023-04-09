import streamlit as st
import PyPDF2
import pdfplumber
import os
from io import BytesIO
from llama_index import download_loader, GPTSimpleVectorIndex, Document


def read_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        pages = []
        for i in range(len(pdf.pages)):
            page = pdf.pages[i]
            text = page.extract_text()
            pages.append(text)
    return pages


def display_youtube_video(url):
    video_id = url.split("watch?v=")[-1]
    st.markdown(
        f'<iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', unsafe_allow_html=True)


def summarize_youtube_video(url, prompt):
    """Takes a url and prompt and delivers response"""
    YoutubeTranscriptReader = download_loader("YoutubeTranscriptReader")
    loader = YoutubeTranscriptReader()
    documents = loader.load_data(ytlinks=[url])
    index = GPTSimpleVectorIndex.from_documents(documents)
    response = index.query(prompt)
    return response


def summarize_wiki_article(page_name, prompt):
    """Takes a pagename and prompt and delivers response"""
    wikipedia_reader = download_loader("WikipediaReader")
    loader = wikipedia_reader()
    wikidocs = loader.load_data(pages=[page_name])
    index = GPTSimpleVectorIndex.from_documents(wikidocs)
    response = index.query(prompt)
    return response


st.set_page_config(page_title="PDF Reader and YouTube Player",
                   layout="wide", initial_sidebar_state="expanded")

st.title("Master Summarizer")
api_key = st.sidebar.text_input("Secret Key: ", type='password')
os.environ['OPENAI_API_KEY'] = api_key

tab_names = ["YouTube", "Wikipedia", "PDF"]
tab_choice = st.sidebar.radio("Choose a Tab", tab_names)

uploaded_files = {}

if api_key:

    if tab_choice == "YouTube":
        youtube_url = st.text_input("Enter a YouTube video link:")
        youtube_prompt = st.text_area(
            "What would you like to know about this video: ")
        if st.button("Submit"):
            if youtube_url and youtube_prompt:
                display_youtube_video(youtube_url)
            response = summarize_youtube_video(youtube_url, youtube_prompt)
            st.success(f"\n\n{response}")
    elif tab_choice == "Wikipedia":
        wiki_url = st.text_input("Enter a Wiki link or tag:").split('/')[-1]
        wiki_prompt = st.text_area(
            f"What would you like to know about this article: ")
        if st.button("Submit"):
            if wiki_url and wiki_prompt:
                response = summarize_wiki_article(wiki_url, wiki_prompt)
                st.success(f"\n\n{response}")
    elif tab_choice == "PDF":
        uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
        pdf_prompt = st.text_area(
            f"What would you like to know about this document: ")
        if st.button("Submit"):
            if uploaded_file is not None:
                pdf_file = BytesIO(uploaded_file.getbuffer())
                pages = read_pdf(pdf_file)
                documents = [Document(p) for p in pages]
                index = GPTSimpleVectorIndex.from_documents(documents)
                response = index.query(pdf_prompt)
                st.success(f"\n\n{response}")
    else:
        st.write("Bad File")
else:
    st.error("No Secret Key Found!!")
