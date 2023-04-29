import streamlit as st
import pandas as pd

def render_csv_page():
    st.subheader("CSV📊")
    # Upload the CSV file
    csv_file = st.file_uploader("Choose a CSV file", type=["csv"])

    if csv_file is not None:
        data = pd.read_csv(csv_file)

        # Display the number of rows and columns in the DataFrame
        st.write(f"Data has {data.shape[0]} rows and {data.shape[1]} columns.")

        # Show the entire DataFrame
        st.write("Full data:")
        st.write(data)