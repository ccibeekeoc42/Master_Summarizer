import streamlit as st
from summarizer import summarize_youtube_video
from speech_eng import text2voice


def display_youtube_video(url):
    """Takes in a url and displays the video"""
    video_id = url.split("watch?v=")[-1]
    st.markdown(
        f'<iframe width="100%" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', unsafe_allow_html=True)


def render_youtube_page(api_key):
    """Takes in an API key and renders the page for the tab"""
    response = ""
    st.subheader("YouTube📺")
    youtube_url = st.text_input("Enter a YouTube video link:")
    if '//m.' in youtube_url: 
        youtube_url = youtube_url.replace('//m.', '//')
    youtube_prompt = st.text_area(
        "What would you like to know about this video: ")
    if st.button("Submit"):
        if youtube_url and youtube_prompt:
            display_youtube_video(youtube_url)
        with st.spinner("generating..."):
            response = summarize_youtube_video(
                youtube_url, youtube_prompt, api_key)
            st.audio(text2voice(str(response)), format="audio/wav")
            st.success(f"\n\n{response}")
        

   
