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
    st.markdown(f"<h5 class='center'><a href='{linkedin_url}' target='_blank'>LinkedIn</a> | <a href='{youtube_url}' target='_blank'>YouTube</a> | <a href='{personal_website_url}' target='_blank'>Website</a></h5>", unsafe_allow_html=True)
    st.markdown("---", unsafe_allow_html=True)
    # Display the Experience
    st.markdown("<h4 class='center'>Experience</h4>", unsafe_allow_html=True)
    st.markdown("<p class='center'>Technical Program Manager at Intel Inc. (2021 - Present).</p>", unsafe_allow_html=True)
    st.markdown("<p class='center'>Senior Software Engineer at Intel Inc. (2021).</p>", unsafe_allow_html=True)
    st.markdown("<p class='center'>Senior Software Dev. & Test Engineer at Cummins Inc. (2017 - 2021).</p>", unsafe_allow_html=True)
    st.markdown("<p class='center'>Dynamic System & Controls Engineering Intern at Cummins Inc. (2017 - 2021).</p>", unsafe_allow_html=True)
    st.markdown("<p class='center'>Research Assistant at TN Tech. (2015 - 2017).</p>", unsafe_allow_html=True)
    st.markdown("---", unsafe_allow_html=True)
    # Display the Publication
    ieee_journal_url = "https://ieeexplore.ieee.org/document/7948779"
    ieee_conferencel_url = "https://ieeexplore.ieee.org/document/7744904"
    elsevier_journal_url = "https://www.sciencedirect.com/science/article/abs/pii/S037877961730041X"
    st.markdown("<h4 class='center'>Publications</h4>", unsafe_allow_html=True)
    st.markdown("<p class='center'><a href='{ieee_journal_url}' target='_blank'>State of Charge and State of Health Estimation for Lithium Batteries Using Recurrent Neural Networks</a>.</p>", unsafe_allow_html=True)
    st.markdown("<p class='center'><a href='{ieee_conferencel_url}' target='_blank'>State of Charge Estimation of LiFePO4 Batteries with Temperature Variations using Neural Networks</a>.</p>", unsafe_allow_html=True)
    st.markdown("<p class='center'><a href='{elsevier_journal_url}' target='_blank'>Aging Prediction and State of Charge Estimation of a LiFePO4 battery using input time-delayed neural networks</a>.</p>", unsafe_allow_html=True)
    st.markdown("---", unsafe_allow_html=True)

    # Display the Education
    thesis_url = "https://www.tntech.edu/engineering/pdf/grad/ms/2017/CIEkeocha_MS.pdf"
    st.markdown("<h4 class='center'>Education</h4>", unsafe_allow_html=True)
    st.markdown("<p class='center'>Master's Degree in Computer Engineering {<a href='{thesis_url}' target='_blank'>Thesis</a>}.</p>", unsafe_allow_html=True)
    st.markdown("<p class='center'>Bachelor of Science in Electrical Engineering.</p>", unsafe_allow_html=True)
    st.markdown("---", unsafe_allow_html=True)

    # Display the Education
    st.markdown("<h4 class='center'>Hobbies</h4>", unsafe_allow_html=True)
    st.markdown("<p class='center'>Leading, Learning, and Educating.</p>", unsafe_allow_html=True)
    st.markdown("<p class='center'>Traveling, Exploring, and Discovering.</p>", unsafe_allow_html=True)
    st.markdown("<p class='center'>Reading, Researching, and Coding.</p>", unsafe_allow_html=True)
    st.markdown("<p class='center'>Food, Fitness, and Wellness.</p>", unsafe_allow_html=True)
    st.markdown("---", unsafe_allow_html=True)
    st.markdown("<h4 class='center'><i>Thank You.</i></h4>", unsafe_allow_html=True)