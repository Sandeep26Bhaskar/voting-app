import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


# Streamlit app title
st.title("CSV file Profiler")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded CSV file
    df = pd.read_csv(uploaded_file)
    st.write("Dataset Preview:")
    st.write(df.head())

    # Generate pandas profiling report
    profile = ProfileReport(df, explorative=True)

    # Display the profiling report in Streamlit
    st_profile_report(profile)
else:
    st.write("Please upload a CSV file to generate the profiling report.")