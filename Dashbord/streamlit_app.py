import streamlit as st

import pandas as pd

# The file config.toml is important for live running
st.title("Sales Streamlit Dashbord")

# st.title("Second Title")
@st.cache_data
def load_data(path:str):
    data = pd.read_excel(path)
    
    return data



# Another option

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is None:
    st.info("Please upload a file to continue")
    st.stop()
    
if uploaded_file:

    df = load_data(uploaded_file)

    st.dataframe(df)




    
    