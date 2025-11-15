import streamlit as st

st.set_page_config(page_title="Data Profiling App", layout="wide")

import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport
from streamlit_ydata_profiling import st_profile_report

st.title("Data Profiling Application")

with st.sidebar:
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        st.write('Mode of operation:')
        minimal  = st.checkbox('Minimal Report', value=False) 

        

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    profile = ProfileReport(df,  minimal = minimal)
    st_profile_report(profile)
