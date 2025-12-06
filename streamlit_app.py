import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

# Configure page
st.set_page_config(
    page_title="Streamlit Demo App",
    page_icon="📊",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.big-font {
    font-size:30px !important;
    font-weight:bold;
}
.medium-font {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Navigation")
app_mode = st.sidebar.selectbox(
    "Choose the app mode",
    ["Home", "Data Visualization", "Interactive Demo", "About"]
)

# Home Page
if app_mode == "Home":
    st.markdown('<p class="big-font">Welcome to Streamlit Demo App</p>', unsafe_allow_html=True)
    
    st.write("""
    This is a demonstration of Streamlit's capabilities including:
    - Interactive widgets
    - Data visualization
    - Layout components
    - File uploading
    """)
    
    image = Image.open('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png')
    st.image(image, caption='Streamlit Logo', width=300)
    
    st.info("👈 Select a demo from the sidebar to get started!")

# Data Visualization Page
elif app_mode == "Data Visualization":
    st.markdown('<p class="big-font
