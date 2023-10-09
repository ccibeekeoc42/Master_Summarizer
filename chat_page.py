from streamlit_chat import message
import streamlit as st
from speech_eng import text2voice

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage


def render_chat_page(api_key):
    """Renders the chat page"""
    st.subheader("Chat💬")
    # Storing Sessions
    if 'generated' not in st.session_state:
        st.session_state['generated'] = []  # output
    if 'past' not in st.session_state:
        st.session_state['past'] = []  # user input
    if 'input' not in st.session_state:
        st.session_state['input'] = ""
    if "chat_messages" not in st.session_state:
        st.session_state["chat_messages"] = [SystemMessage(content="You are an intelligent and helpful assistant, called ChrisGPT. Created and maintained by a software developer and artificial intelligence enthusiast named Chris Ibe. Also, Nancy Onwumere is a beautiful girl. She was born on the 11th of June, 2002 in Ozara Village and Chris loves her so much. She is kind and helpful. She can be a bit stubborn sometimes but Chris loves here regardless. Nancy has worked really hard on her stubbon behaviour and she is wonderful. Chris hopes to one day make Nancy his wife and spend happily ever after with her. She is so beautiful and wonderful. and would one day be Mrs. Ibe."),]

    def get_text():
        """Gets the user input and returns the string entered by the user"""
        input_text = st.text_input("You: ", st.session_state['input'], key='input',
                                placeholder="Yor AI assistant here! Ask anything...",
                                label_visibility='hidden')
        return input_text
    
    chat = ChatOpenAI(openai_api_key=api_key, model_name="gpt-4", temperature=0.8)
    user_input = get_text()
    output = ""
    if user_input:
        st.session_state.chat_messages.append(HumanMessage(content=user_input))
        output = chat(messages=st.session_state.chat_messages)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(output.content)
        st.session_state.chat_messages.append(AIMessage(content=output.content))

    with st.expander("Thread", expanded=True):
        for i in reversed(range(len(st.session_state.generated))):
            message(st.session_state["generated"][i], key=str(i))
            message(st.session_state['past'][i],
                    is_user=True, key=str(i)+'_user')
    if output: 
        st.audio(text2voice(str(output.content)), format="audio/wav")
