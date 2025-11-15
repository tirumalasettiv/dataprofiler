import streamlit as st

st.set_page_config(page_title="Data Profiling App", layout="wide")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

with st.sidebar:
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        st.write('Mode of operation:')
        minimal  = st.checkbox('Minimal Report', value=False) 
        display_mode = st.radio( 'Display Mode', ('Primary', 'Dark', 'Orange'))
        
        if display_mode == 'Dark':
            dark_mode = True
            orange_mode = False
        elif display_mode == 'Orange':
            dark_mode = False
            orange_mode = True
        else:
            dark_mode = False
            orange_mode = False
        
        

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    profile = ProfileReport(df,  minimal = minimal)
    st_profile_report(profile)
