import streamlit as st

import pandas as pd

import time


def main():

    st.write("# :green[WELCOME TO MY FIRST STREAMLIT  APPLICATION]")

    # col1, col2, col3 = st.columns(3)

    col1, col2, col3 = st.columns([1,2,1])


    with col1:
        st.header("This is the header for the first column")
        
        
    with col2:
        st.header("This is the header for the column 2")
        
        
    with col3:
        st.header("This is the header for the column 3")

    capture_img = col1.camera_input('Take a picture')
    
    if capture_img is not None:
        
        st.success('Picture taked successfully')
        
        capture_img
    
    
    while True:
        st.write("I strive to be my best possible")

        # Sleep for 1 hour before scraping again
        time.sleep(15)  # 3600 seconds = 1 hour
    
    
if __name__ == '__main__':
    main()







