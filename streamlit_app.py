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
    st.markdown('<p class="big-font">Data Visualization Dashboard</p>', unsafe_allow_html=True)
    
    # Generate sample data
    @st.cache_data
    def load_data():
        data = pd.DataFrame({
            'Date': pd.date_range('2023-01-01', periods=100),
            'Sales': np.random.randint(100, 500, 100),
            'Profit': np.random.randint(10, 50, 100),
            'Region': np.random.choice(['North', 'South', 'East', 'West'], 100)
        })
        return data
    
    df = load_data()
    
    # Filters
    st.sidebar.header("Filters")
    region_filter = st.sidebar.multiselect("Select Region", df['Region'].unique(), df['Region'].unique())
    date_range = st.sidebar.date_input("Select Date Range", [df['Date'].min(), df['Date'].max()])
    
    # Apply filters
    filtered_df = df[
        (df['Region'].isin(region_filter)) & 
        (df['Date'] >= pd.to_datetime(date_range[0])) & 
        (df['Date'] <= pd.to_datetime(date_range[1]))
    ]
    
    # Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Sales", f"${filtered_df['Sales'].sum():,}")
    col2.metric("Average Profit", f"${filtered_df['Profit'].mean():.2f}")
    col3.metric("Transactions", len(filtered_df))
    
    # Charts
    st.subheader("Sales Over Time")
    fig1, ax1 = plt.subplots(figsize=(10, 4))
    ax1.plot(filtered_df['Date'], filtered_df['Sales'], marker='o', linewidth=2)
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Sales')
    st.pyplot(fig1)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Sales by Region")
        fig2, ax2 = plt.subplots()
        region_sales = filtered_df.groupby('Region')['Sales'].sum()
        ax2.pie(region_sales, labels=region_sales.index, autopct='%1.1f%%')
        st.pyplot(fig2)
    
    with col2:
        st.subheader("Profit Distribution")
        fig3, ax3 = plt.subplots()
        ax3.hist(filtered_df['Profit'], bins=20, color='skyblue', edgecolor='black')
        ax3.set_xlabel('Profit')
        ax3.set_ylabel('Frequency')
        st.pyplot(fig3)
    
    # Data table
    st.subheader("Data Table")
    st.dataframe(filtered_df.style.highlight_max(axis=0))

# Interactive Demo Page
elif app_mode == "Interactive Demo":
    st.markdown('<p class="big-font">Interactive Widgets Demo</p>', unsafe_allow_html=True)
    
    # Text inputs
    st.subheader("Text Inputs")
    name = st.text_input("Enter your name", "John Doe")
    age = st.slider("Select your age", 18, 100, 25)
    st.write(f"Hello {name}, you are {age} years old!")
    
    # File uploader
    st.subheader("File Uploader")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Uploaded Data:")
        st.dataframe(df.head())
    
    # Interactive plot
    st.subheader("Interactive Plot")
    plot_type = st.selectbox("Select plot type", ["Line", "Bar", "Scatter"])
    x_points = st.slider("Number of data points", 10, 100, 50)
    
    # Generate data
    x = np.linspace(0, 10, x_points)
    y = np.sin(x) * np.random.rand(x_points)
    
    # Create plot
    fig, ax = plt.subplots()
    if plot_type == "Line":
        ax.plot(x, y, marker='o')
    elif plot_type == "Bar":
        ax.bar(x, y)
    else:
        ax.scatter(x, y)
    
    ax.set_xlabel("X Values")
    ax.set_ylabel("Y Values")
    st.pyplot(fig)
    
    # Checkbox and radio buttons
    st.subheader("Additional Options")
    if st.checkbox("Show detailed stats"):
        st.write(f"Mean: {np.mean(y):.2f}")
        st.write(f"Standard Deviation: {np.std(y):.2f}")
        st.write(f"Min: {np.min(y):.2f}")
        st.write(f"Max: {np.max(y):.2f}")
    
    option = st.radio("Choose a color", ["Red", "Green", "Blue"])
    st.write(f"You selected: {option}")

# About Page
else:
    st.markdown('<p class="big-font">About This App</p>', unsafe_allow_html=True)
    
    st.write("""
    This demo app showcases various Streamlit features:
    
    ### Features Demonstrated:
    - Multi-page navigation
    - Interactive widgets (sliders, checkboxes, file uploader)
    - Data visualization with Matplotlib
    - Responsive layout with columns
    - Caching for performance
    - Custom styling with CSS
    - Data filtering and metrics
    
    ### How to Use:
    1. Navigate between sections using the sidebar
    2. Interact with widgets to see dynamic updates
    3. Upload your own CSV files in the Interactive Demo
    4. Apply filters in the Data Visualization section
    
    ### Requirements:
    ```
    streamlit
    pandas
    numpy
    matplotlib
    seaborn
    pillow
    ```
    """)

    st.info("Built with ❤️ using [Streamlit](https://streamlit.io)")

# Footer
st.markdown("---")
st.caption("Streamlit Demo App • Created with Streamlit")
