import streamlit as st
from PIL import Image
from io import BytesIO
import base64

def render_profile_page():
    # Custom CSS for center alignment
    st.markdown(
        """
        <style>
            .center {
                display: block;
                margin-left: auto;
                margin-right: auto;
                text-align: center;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Load the profile picture from a local file
    profile_pic_path = "chris.png"
    profile_pic = Image.open(profile_pic_path)

    # Convert the image to base64
    buffered = BytesIO()
    profile_pic.save(buffered, format="PNG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

    # Display the profile picture in a circular shape, centered
    st.markdown(f'<div class="center"><img src="data:image/png;base64,{img_base64}" alt="Profile Picture" style="border-radius: 50%;"></div>', unsafe_allow_html=True)

    # Display links to LinkedIn, YouTube, and personal website
    linkedin_url = "https://www.linkedin.com/in/christopher-ibe-ekeocha/"
    youtube_url = "https://www.youtube.com/channel/UCOj48N8EeWNBZOGsI2ywFUQ"
    personal_website_url = "https://ccibeekeoc42.github.io/resume/"

    # Display the person's name and bio, centered
    st.markdown("<h1 class='center'>Chris Ibe</h1>", unsafe_allow_html=True)
    st.markdown("<p class='center'>I am a proficient Software Engineering/ Machine Learning Program Manager (PM) with both technical and innovative problem solving skills to drive projects through entire lifecycles. Experienced with leading teams, communicating with clients, and generating solutions that not only impact broad userbase, but also yield high returns on investment.</p>", unsafe_allow_html=True)
    
    # Display the person's name and bio
    st.markdown(f"<h4 class='center'><a href='{linkedin_url}' target='_blank'>LinkedIn</a> | <a href='{youtube_url}' target='_blank'>YouTube</a> | <a href='{personal_website_url}' target='_blank'>Website</a></h4>", unsafe_allow_html=True)