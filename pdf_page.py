import streamlit as st
from summarizer import summarize_pdf
from speech_eng import text2voice


def render_pdf_page(api_key):
    st.subheader("PDF📑")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    pdf_prompt = st.text_area(
        f"What would you like to know about this document: ")
    if st.button("Submit"):
        if uploaded_file is not None and pdf_prompt:
            with st.spinner("generating..."):
                response = summarize_pdf(uploaded_file, pdf_prompt, api_key)
                st.audio(text2voice(str(response)), format="audio/wav")
                st.success(f"\n\n{response}")
