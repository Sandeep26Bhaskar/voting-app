import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
import os
from pathlib import Path



def profiler():
    st.title("Data Profiler")

    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
            st.subheader("Data Preview")
            st.dataframe(df.head())

            with st.spinner("Generating report..."):
                profile = ProfileReport(df, title="Data Profile Report", explorative=True)
                profile.to_file("report.html")

            # Display download link or open in new tab
            st.success("Report generated successfully.")
            with open("report.html", "r", encoding="utf-8") as f:
                st.download_button("Download Full Report", data=f, file_name=f"{Path(uploaded_file.name).stem}.html", mime="text/html")

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.info("Upload a CSV file to begin.")
