import streamlit as st
from summarizer import summarize_wiki_article


def render_wikipedia_page(api_key):
    st.subheader("Wikipedia📃")
    wiki_url = st.text_input("Enter a Wiki link or tag:").split('/')[-1]
    wiki_prompt = st.text_area(
        f"What would you like to know about this article: ")
    if st.button("Submit"):
        if wiki_url and wiki_prompt:
            with st.spinner("generating..."):
                response = summarize_wiki_article(
                    wiki_url, wiki_prompt, api_key)
            st.success(f"\n\n{response}")
