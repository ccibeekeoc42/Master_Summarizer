import streamlit as st
import pandas as pd
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

def render_csv_page(api_key):
    st.subheader("CSV📊")
    # Upload the CSV file
    csv_file = st.file_uploader("Choose a CSV file", type=["csv"])
    if csv_file:
        data = pd.read_csv(csv_file)
        data.to_csv('temp.csv')
    csv_prompt = st.text_area(f"What would you like to know: ")
    if st.button("Submit"):
        if csv_file and csv_prompt:
            with st.spinner("generating..."):
                # creating the agent
                agent = create_csv_agent(
                    ChatOpenAI(openai_api_key=api_key, temperature=0.75, model_name="gpt-4"),
                    'temp.csv',
                    verbose=False
                )
                st.success(agent.run(csv_prompt))

                # Display the number of rows and columns in the DataFrame
                st.write(f"Data has {data.shape[0]} rows and {data.shape[1]} columns.")

            # Show the entire DataFrame
            st.write("Full data:")
            st.write(data)