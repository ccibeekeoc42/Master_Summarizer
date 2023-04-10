import streamlit as st
from summarizer import summarize_youtube_video


def display_youtube_video(url):
    """Takes in a url and displays the video"""
    video_id = url.split("watch?v=")[-1]
    st.markdown(
        f'<iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', unsafe_allow_html=True)


def render_youtube_page(api_key):
    """Takes in an API key and renders the page for the tab"""
    st.subheader("YouTube📺")
    youtube_url = st.text_input("Enter a YouTube video link:")
    youtube_prompt = st.text_area(
        "What would you like to know about this video: ")
    if st.button("Submit"):
        if youtube_url and youtube_prompt:
            display_youtube_video(youtube_url)
        with st.spinner("generating..."):
            response = summarize_youtube_video(
                youtube_url, youtube_prompt, api_key)
        st.success(f"\n\n{response}")
