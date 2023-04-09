import streamlit as st
import PyPDF2
import os
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationEntityMemory
from langchain.chains.conversation.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE
from langchain.llms import OpenAI
from streamlit_chat import message
from summarizer import summarize_youtube_video, summarize_wiki_article, summarize_pdf


def display_youtube_video(url):
    video_id = url.split("watch?v=")[-1]
    st.markdown(
        f'<iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', unsafe_allow_html=True)


st.set_page_config(page_title="PDF Reader and YouTube Player",
                   layout="wide", initial_sidebar_state="expanded")

st.title("Master Summarizer")
api_key = st.sidebar.text_input("Secret Key: ", type='password')
os.environ['OPENAI_API_KEY'] = api_key

tab_names = ["YouTube", "Wikipedia", "PDF", "Chat"]
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
            if uploaded_file is not None and pdf_prompt:
                response = summarize_pdf(uploaded_file, pdf_prompt)
                st.success(f"\n\n{response}")
    elif tab_choice == "Chat":
        # Storing Sessions
        if 'generated' not in st.session_state:
            st.session_state['generated'] = []  # output
        if 'past' not in st.session_state:
            st.session_state['past'] = []  # user input
        if 'input' not in st.session_state:
            st.session_state['input'] = ""
        if "stored_session" not in st.session_state:
            st.session_state["stored_session"] = []

        def get_text():
            """Gets the user input and returns the string entered by the user"""
            input_text = st.text_input("You: ", st.session_state['input'], key='input',
                                       placeholder="Yor AI assistant here! Ask anything...",
                                       label_visibility='hidden')
            return input_text

        llm = OpenAI(openai_api_key=api_key, temperature=0.5,
                     model_name='gpt-3.5-turbo')
        # create conv memory
        if 'entity_memory' not in st.session_state:
            st.session_state['entity_memory'] = ConversationEntityMemory(
                llm=llm, k=10)
        # Create conversation chain
        conversation = ConversationChain(
            llm=llm,
            prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE,
            memory=st.session_state['entity_memory'])
        user_input = get_text()
        if user_input:
            output = conversation.run(input=user_input)
            st.session_state.past.append(user_input)
            st.session_state.generated.append(output)

        with st.expander("Thread", expanded=True):
            for i in reversed(range(len(st.session_state.generated))):
                message(st.session_state["generated"][i], key=str(i))
                message(st.session_state['past'][i],
                        is_user=True, key=str(i)+'_user')
    else:
        st.write("Bad File")
else:
    st.error("No Secret Key Found!!")
