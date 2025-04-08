import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit.components.v1 import html

st.set_page_config(page_title="📊 Data Profiler", layout="wide")
st.title("📊 Data Profiler")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("🧾 Data Preview")
    st.dataframe(df.head())

    with st.spinner("Generating profiling report..."):
        profile = ProfileReport(df, title="Data Profiling Report", explorative=True)
        profile_html = profile.to_html()
        html(profile_html, height=1000, scrolling=True)
else:
    st.info("👆 Please upload a CSV file to begin.")
