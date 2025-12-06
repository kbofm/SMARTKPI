import streamlit as st
import pandas as pd
import numpy as np

# Configure page
st.set_page_config(
    page_title="SmartKPI Dashboard",
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
    ["Home", "KPI Dashboard", "Data Analysis", "About"]
)

# Home Page
if app_mode == "Home":
    st.markdown('<p class="big-font">Welcome to SmartKPI Dashboard</p>', unsafe_allow_html=True)
    
    st.write("""
    This is a SmartKPI dashboard application built with Streamlit.
    
    ### Features:
    - Real-time KPI monitoring
    - Interactive data analysis
    - Customizable metrics
    - Responsive design
    """)
    
    st.info("👈 Select a section from the sidebar to get started!")

# KPI Dashboard Page
elif app_mode == "KPI Dashboard":
    st.markdown('<p class="big-font">KPI Dashboard</p>', unsafe_allow_html=True)
    
    # Generate sample data
    @st.cache_data
    def load_kpi_data():
        data = pd.DataFrame({
            'Date': pd.date_range('2023-01-01', periods=50),
            'Revenue': np.random.randint(1000, 5000, 50),
            'Customers': np.random.randint(50, 200, 50),
            'Conversion': np.random.uniform(1.5, 5.0, 50),
            'Satisfaction': np.random.uniform(3.0, 5.0, 50)
        })
        return data
    
    df = load_kpi_data()
    
    # Filters
    st.sidebar.header("Filters")
    date_range = st.sidebar.date_input("Select Date Range", 
                                      [df['Date'].min(), df['Date'].max()])
    
    # Apply filters
    filtered_df = df[
        (df['Date'] >= pd.to_datetime(date_range[0])) & 
        (df['Date'] <= pd.to_datetime(date_range[1]))
    ]
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Revenue", f"${filtered_df['Revenue'].sum():,}")
    col2.metric("Avg Customers", f"{filtered_df['Customers'].mean():.0f}")
    col3.metric("Avg Conversion", f"{filtered_df['Conversion'].mean():.2f}%")
    col4.metric("Satisfaction", f"{filtered_df['Satisfaction'].mean():.2f}/5")
    
    # KPI Charts using Streamlit's built-in charts
    st.subheader("Revenue Trend")
    st.line_chart(filtered_df.set_index('Date')['Revenue'])
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Customers Over Time")
        st.bar_chart(filtered_df.set_index('Date')['Customers'])
    
    with col2:
        st.subheader("Conversion Rate")
        st.area_chart(filtered_df.set_index('Date')['Conversion'])
    
    # Data table
    st.subheader("KPI Data")
    st.dataframe(filtered_df.style.highlight_max(axis=0))

# Data Analysis Page
elif app_mode == "Data Analysis":
    st.markdown('<p class="big-font">Data Analysis</p>', unsafe_allow_html=True)
    
    # Text inputs
    st.subheader("KPI Configuration")
    kpi_name = st.text_input("KPI Name", "Customer Acquisition Cost")
    target_value = st.number_input("Target Value", value=50.0)
    current_value = st.number_input("Current Value", value=45.6)
    
    # Calculate variance
    variance = current_value - target_value
    variance_pct = (variance / target_value) * 100 if target_value != 0 else 0
    
    st.write(f"**{kpi_name}**")
    st.metric("Variance", f"{variance:.2f}", f"{variance_pct:.2f}%")
    
    # File uploader
    st.subheader("Upload KPI Data")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Uploaded Data:")
        st.dataframe(df.head())
        
        # If numeric columns exist, show basic stats
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            st.subheader("Data Summary")
            st.write(df[numeric_cols].describe())
    
    # Interactive controls
    st.subheader("Simulation Controls")
    simulation_type = st.selectbox("Select Analysis Type", 
                                  ["Trend Analysis", "Variance Report", "Forecast"])
    data_points = st.slider("Number of Data Points", 10, 100, 30)
    
    # Generate sample data for visualization
    x = np.arange(data_points)
    y = np.cumsum(np.random.randn(data_points)) + 100
    
    # Create chart data
    chart_data = pd.DataFrame({
        'x': x,
        'y': y
    })
    
    st.subheader(f"{simulation_type} Results")
    st.line_chart(chart_data.set_index('x'))

# About Page
else:
    st.markdown('<p class="big-font">About SmartKPI</p>', unsafe_allow_html=True)
    
    st.write("""
    ### SmartKPI Dashboard
    
    This application provides a comprehensive dashboard for monitoring 
    key performance indicators with real-time data visualization.
    
    ### Key Features:
    - Interactive KPI monitoring
    - Customizable dashboards
    - Data filtering and analysis
    - Export capabilities
    - Responsive design for all devices
    
    ### Technology Stack:
    - Streamlit for the web framework
    - Pandas for data manipulation
    - NumPy for numerical computations
    
    ### How to Use:
    1. Navigate using the sidebar menu
    2. Apply filters to customize views
    3. Upload your own data for analysis
    4. Configure KPIs based on your needs
    """)

    st.info("Built with ❤️ using [Streamlit](https://streamlit.io)")

# Footer
st.markdown("---")
st.caption("SmartKPI Dashboard • Real-time Performance Monitoring")
import streamlit as st
import pandas as pd
import numpy as np

# Configure page
st.set_page_config(
    page_title="SmartKPI Dashboard",
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
    ["Home", "KPI Dashboard", "Data Analysis", "About"]
)

# Home Page
if app_mode == "Home":
    st.markdown('<p class="big-font">Welcome to SmartKPI Dashboard</p>', unsafe_allow_html=True)
    
    st.write("""
    This is a SmartKPI dashboard application built with Streamlit.
    
    ### Features:
    - Real-time KPI monitoring
    - Interactive data analysis
    - Customizable metrics
    - Responsive design
    """)
    
    st.info("👈 Select a section from the sidebar to get started!")

# KPI Dashboard Page
elif app_mode == "KPI Dashboard":
    st.markdown('<p class="big-font">KPI Dashboard</p>', unsafe_allow_html=True)
    
    # Generate sample data
    @st.cache_data
    def load_kpi_data():
        data = pd.DataFrame({
            'Date': pd.date_range('2023-01-01', periods=50),
            'Revenue': np.random.randint(1000, 5000, 50),
            'Customers': np.random.randint(50, 200, 50),
            'Conversion': np.random.uniform(1.5, 5.0, 50),
            'Satisfaction': np.random.uniform(3.0, 5.0, 50)
        })
        return data
    
    df = load_kpi_data()
    
    # Filters
    st.sidebar.header("Filters")
    date_range = st.sidebar.date_input("Select Date Range", 
                                      [df['Date'].min(), df['Date'].max()])
    
    # Apply filters
    filtered_df = df[
        (df['Date'] >= pd.to_datetime(date_range[0])) & 
        (df['Date'] <= pd.to_datetime(date_range[1]))
    ]
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Revenue", f"${filtered_df['Revenue'].sum():,}")
    col2.metric("Avg Customers", f"{filtered_df['Customers'].mean():.0f}")
    col3.metric("Avg Conversion", f"{filtered_df['Conversion'].mean():.2f}%")
    col4.metric("Satisfaction", f"{filtered_df['Satisfaction'].mean():.2f}/5")
    
    # KPI Charts using Streamlit's built-in charts
    st.subheader("Revenue Trend")
    st.line_chart(filtered_df.set_index('Date')['Revenue'])
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Customers Over Time")
        st.bar_chart(filtered_df.set_index('Date')['Customers'])
    
    with col2:
        st.subheader("Conversion Rate")
        st.area_chart(filtered_df.set_index('Date')['Conversion'])
    
    # Data table
    st.subheader("KPI Data")
    st.dataframe(filtered_df.style.highlight_max(axis=0))

# Data Analysis Page
elif app_mode == "Data Analysis":
    st.markdown('<p class="big-font">Data Analysis</p>', unsafe_allow_html=True)
    
    # Text inputs
    st.subheader("KPI Configuration")
    kpi_name = st.text_input("KPI Name", "Customer Acquisition Cost")
    target_value = st.number_input("Target Value", value=50.0)
    current_value = st.number_input("Current Value", value=45.6)
    
    # Calculate variance
    variance = current_value - target_value
    variance_pct = (variance / target_value) * 100 if target_value != 0 else 0
    
    st.write(f"**{kpi_name}**")
    st.metric("Variance", f"{variance:.2f}", f"{variance_pct:.2f}%")
    
    # File uploader
    st.subheader("Upload KPI Data")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Uploaded Data:")
        st.dataframe(df.head())
        
        # If numeric columns exist, show basic stats
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            st.subheader("Data Summary")
            st.write(df[numeric_cols].describe())
    
    # Interactive controls
    st.subheader("Simulation Controls")
    simulation_type = st.selectbox("Select Analysis Type", 
                                  ["Trend Analysis", "Variance Report", "Forecast"])
    data_points = st.slider("Number of Data Points", 10, 100, 30)
    
    # Generate sample data for visualization
    x = np.arange(data_points)
    y = np.cumsum(np.random.randn(data_points)) + 100
    
    # Create chart data
    chart_data = pd.DataFrame({
        'x': x,
        'y': y
    })
    
    st.subheader(f"{simulation_type} Results")
    st.line_chart(chart_data.set_index('x'))

# About Page
else:
    st.markdown('<p class="big-font">About SmartKPI</p>', unsafe_allow_html=True)
    
    st.write("""
    ### SmartKPI Dashboard
    
    This application provides a comprehensive dashboard for monitoring 
    key performance indicators with real-time data visualization.
    
    ### Key Features:
    - Interactive KPI monitoring
    - Customizable dashboards
    - Data filtering and analysis
    - Export capabilities
    - Responsive design for all devices
    
    ### Technology Stack:
    - Streamlit for the web framework
    - Pandas for data manipulation
    - NumPy for numerical computations
    
    ### How to Use:
    1. Navigate using the sidebar menu
    2. Apply filters to customize views
    3. Upload your own data for analysis
    4. Configure KPIs based on your needs
    """)

    st.info("Built with ❤️ using [Streamlit](https://streamlit.io)")

# Footer
st.markdown("---")
st.caption("SmartKPI Dashboard • Real-time Performance Monitoring")
import streamlit as st
import pandas as pd
import numpy as np

# Configure page
st.set_page_config(
    page_title="SmartKPI Dashboard",
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
    ["Home", "KPI Dashboard", "Data Analysis", "About"]
)

# Home Page
if app_mode == "Home":
    st.markdown('<p class="big-font">Welcome to SmartKPI Dashboard</p>', unsafe_allow_html=True)
    
    st.write("""
    This is a SmartKPI dashboard application built with Streamlit.
    
    ### Features:
    - Real-time KPI monitoring
    - Interactive data analysis
    - Customizable metrics
    - Responsive design
    """)
    
    st.info("👈 Select a section from the sidebar to get started!")

# KPI Dashboard Page
elif app_mode == "KPI Dashboard":
    st.markdown('<p class="big-font">KPI Dashboard</p>', unsafe_allow_html=True)
    
    # Generate sample data
    @st.cache_data
    def load_kpi_data():
        data = pd.DataFrame({
            'Date': pd.date_range('2023-01-01', periods=50),
            'Revenue': np.random.randint(1000, 5000, 50),
            'Customers': np.random.randint(50, 200, 50),
            'Conversion': np.random.uniform(1.5, 5.0, 50),
            'Satisfaction': np.random.uniform(3.0, 5.0, 50)
        })
        return data
    
    df = load_kpi_data()
    
    # Filters
    st.sidebar.header("Filters")
    date_range = st.sidebar.date_input("Select Date Range", 
                                      [df['Date'].min(), df['Date'].max()])
    
    # Apply filters
    filtered_df = df[
        (df['Date'] >= pd.to_datetime(date_range[0])) & 
        (df['Date'] <= pd.to_datetime(date_range[1]))
    ]
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Revenue", f"${filtered_df['Revenue'].sum():,}")
    col2.metric("Avg Customers", f"{filtered_df['Customers'].mean():.0f}")
    col3.metric("Avg Conversion", f"{filtered_df['Conversion'].mean():.2f}%")
    col4.metric("Satisfaction", f"{filtered_df['Satisfaction'].mean():.2f}/5")
    
    # KPI Charts using Streamlit's built-in charts
    st.subheader("Revenue Trend")
    st.line_chart(filtered_df.set_index('Date')['Revenue'])
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Customers Over Time")
        st.bar_chart(filtered_df.set_index('Date')['Customers'])
    
    with col2:
        st.subheader("Conversion Rate")
        st.area_chart(filtered_df.set_index('Date')['Conversion'])
    
    # Data table
    st.subheader("KPI Data")
    st.dataframe(filtered_df.style.highlight_max(axis=0))

# Data Analysis Page
elif app_mode == "Data Analysis":
    st.markdown('<p class="big-font">Data Analysis</p>', unsafe_allow_html=True)
    
    # Text inputs
    st.subheader("KPI Configuration")
    kpi_name = st.text_input("KPI Name", "Customer Acquisition Cost")
    target_value = st.number_input("Target Value", value=50.0)
    current_value = st.number_input("Current Value", value=45.6)
    
    # Calculate variance
    variance = current_value - target_value
    variance_pct = (variance / target_value) * 100 if target_value != 0 else 0
    
    st.write(f"**{kpi_name}**")
    st.metric("Variance", f"{variance:.2f}", f"{variance_pct:.2f}%")
    
    # File uploader
    st.subheader("Upload KPI Data")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Uploaded Data:")
        st.dataframe(df.head())
        
        # If numeric columns exist, show basic stats
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            st.subheader("Data Summary")
            st.write(df[numeric_cols].describe())
    
    # Interactive controls
    st.subheader("Simulation Controls")
    simulation_type = st.selectbox("Select Analysis Type", 
                                  ["Trend Analysis", "Variance Report", "Forecast"])
    data_points = st.slider("Number of Data Points", 10, 100, 30)
    
    # Generate sample data for visualization
    x = np.arange(data_points)
    y = np.cumsum(np.random.randn(data_points)) + 100
    
    # Create chart data
    chart_data = pd.DataFrame({
        'x': x,
        'y': y
    })
    
    st.subheader(f"{simulation_type} Results")
    st.line_chart(chart_data.set_index('x'))

# About Page
else:
    st.markdown('<p class="big-font">About SmartKPI</p>', unsafe_allow_html=True)
    
    st.write("""
    ### SmartKPI Dashboard
    
    This application provides a comprehensive dashboard for monitoring 
    key performance indicators with real-time data visualization.
    
    ### Key Features:
    - Interactive KPI monitoring
    - Customizable dashboards
    - Data filtering and analysis
    - Export capabilities
    - Responsive design for all devices
    
    ### Technology Stack:
    - Streamlit for the web framework
    - Pandas for data manipulation
    - NumPy for numerical computations
    
    ### How to Use:
    1. Navigate using the sidebar menu
    2. Apply filters to customize views
    3. Upload your own data for analysis
    4. Configure KPIs based on your needs
    """)

    st.info("Built with ❤️ using [Streamlit](https://streamlit.io)")

# Footer
st.markdown("---")
st.caption("SmartKPI Dashboard • Real-time Performance Monitoring")
import streamlit as st
import pandas as pd
import numpy as np

# Configure page
st.set_page_config(
    page_title="SmartKPI Dashboard",
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
    ["Home", "KPI Dashboard", "Data Analysis", "About"]
)

# Home Page
if app_mode == "Home":
    st.markdown('<p class="big-font">Welcome to SmartKPI Dashboard</p>', unsafe_allow_html=True)
    
    st.write("""
    This is a SmartKPI dashboard application built with Streamlit.
    
    ### Features:
    - Real-time KPI monitoring
    - Interactive data analysis
    - Customizable metrics
    - Responsive design
    """)
    
    st.info("👈 Select a section from the sidebar to get started!")

# KPI Dashboard Page
elif app_mode == "KPI Dashboard":
    st.markdown('<p class="big-font">KPI Dashboard</p>', unsafe_allow_html=True)
    
    # Generate sample data
    @st.cache_data
    def load_kpi_data():
        data = pd.DataFrame({
            'Date': pd.date_range('2023-01-01', periods=50),
            'Revenue': np.random.randint(1000, 5000, 50),
            'Customers': np.random.randint(50, 200, 50),
            'Conversion': np.random.uniform(1.5, 5.0, 50),
            'Satisfaction': np.random.uniform(3.0, 5.0, 50)
        })
        return data
    
    df = load_kpi_data()
    
    # Filters
    st.sidebar.header("Filters")
    date_range = st.sidebar.date_input("Select Date Range", 
                                      [df['Date'].min(), df['Date'].max()])
    
    # Apply filters
    filtered_df = df[
        (df['Date'] >= pd.to_datetime(date_range[0])) & 
        (df['Date'] <= pd.to_datetime(date_range[1]))
    ]
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Revenue", f"${filtered_df['Revenue'].sum():,}")
    col2.metric("Avg Customers", f"{filtered_df['Customers'].mean():.0f}")
    col3.metric("Avg Conversion", f"{filtered_df['Conversion'].mean():.2f}%")
    col4.metric("Satisfaction", f"{filtered_df['Satisfaction'].mean():.2f}/5")
    
    # KPI Charts using Streamlit's built-in charts
    st.subheader("Revenue Trend")
    st.line_chart(filtered_df.set_index('Date')['Revenue'])
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Customers Over Time")
        st.bar_chart(filtered_df.set_index('Date')['Customers'])
    
    with col2:
        st.subheader("Conversion Rate")
        st.area_chart(filtered_df.set_index('Date')['Conversion'])
    
    # Data table
    st.subheader("KPI Data")
    st.dataframe(filtered_df.style.highlight_max(axis=0))

# Data Analysis Page
elif app_mode == "Data Analysis":
    st.markdown('<p class="big-font">Data Analysis</p>', unsafe_allow_html=True)
    
    # Text inputs
    st.subheader("KPI Configuration")
    kpi_name = st.text_input("KPI Name", "Customer Acquisition Cost")
    target_value = st.number_input("Target Value", value=50.0)
    current_value = st.number_input("Current Value", value=45.6)
    
    # Calculate variance
    variance = current_value - target_value
    variance_pct = (variance / target_value) * 100 if target_value != 0 else 0
    
    st.write(f"**{kpi_name}**")
    st.metric("Variance", f"{variance:.2f}", f"{variance_pct:.2f}%")
    
    # File uploader
    st.subheader("Upload KPI Data")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Uploaded Data:")
        st.dataframe(df.head())
        
        # If numeric columns exist, show basic stats
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            st.subheader("Data Summary")
            st.write(df[numeric_cols].describe())
    
    # Interactive controls
    st.subheader("Simulation Controls")
    simulation_type = st.selectbox("Select Analysis Type", 
                                  ["Trend Analysis", "Variance Report", "Forecast"])
    data_points = st.slider("Number of Data Points", 10, 100, 30)
    
    # Generate sample data for visualization
    x = np.arange(data_points)
    y = np.cumsum(np.random.randn(data_points)) + 100
    
    # Create chart data
    chart_data = pd.DataFrame({
        'x': x,
        'y': y
    })
    
    st.subheader(f"{simulation_type} Results")
    st.line_chart(chart_data.set_index('x'))

# About Page
else:
    st.markdown('<p class="big-font">About SmartKPI</p>', unsafe_allow_html=True)
    
    st.write("""
    ### SmartKPI Dashboard
    
    This application provides a comprehensive dashboard for monitoring 
    key performance indicators with real-time data visualization.
    
    ### Key Features:
    - Interactive KPI monitoring
    - Customizable dashboards
    - Data filtering and analysis
    - Export capabilities
    - Responsive design for all devices
    
    ### Technology Stack:
    - Streamlit for the web framework
    - Pandas for data manipulation
    - NumPy for numerical computations
    
    ### How to Use:
    1. Navigate using the sidebar menu
    2. Apply filters to customize views
    3. Upload your own data for analysis
    4. Configure KPIs based on your needs
    """)

    st.info("Built with ❤️ using [Streamlit](https://streamlit.io)")

# Footer
st.markdown("---")
st.caption("SmartKPI Dashboard • Real-time Performance Monitoring")
import streamlit as st
import pandas as pd
import numpy as np

# Configure page
st.set_page_config(
    page_title="SmartKPI Dashboard",
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
    ["Home", "KPI Dashboard", "Data Analysis", "About"]
)

# Home Page
if app_mode == "Home":
    st.markdown('<p class="big-font">Welcome to SmartKPI Dashboard</p>', unsafe_allow_html=True)
    
    st.write("""
    This is a SmartKPI dashboard application built with Streamlit.
    
    ### Features:
    - Real-time KPI monitoring
    - Interactive data analysis
    - Customizable metrics
    - Responsive design
    """)
    
    st.info("👈 Select a section from the sidebar to get started!")

# KPI Dashboard Page
elif app_mode == "KPI Dashboard":
    st.markdown('<p class="big-font">KPI Dashboard</p>', unsafe_allow_html=True)
    
    # Generate sample data
    @st.cache_data
    def load_kpi_data():
        data = pd.DataFrame({
            'Date': pd.date_range('2023-01-01', periods=50),
            'Revenue': np.random.randint(1000, 5000, 50),
            'Customers': np.random.randint(50, 200, 50),
            'Conversion': np.random.uniform(1.5, 5.0, 50),
            'Satisfaction': np.random.uniform(3.0, 5.0, 50)
        })
        return data
    
    df = load_kpi_data()
    
    # Filters
    st.sidebar.header("Filters")
    date_range = st.sidebar.date_input("Select Date Range", 
                                      [df['Date'].min(), df['Date'].max()])
    
    # Apply filters
    filtered_df = df[
        (df['Date'] >= pd.to_datetime(date_range[0])) & 
        (df['Date'] <= pd.to_datetime(date_range[1]))
    ]
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Revenue", f"${filtered_df['Revenue'].sum():,}")
    col2.metric("Avg Customers", f"{filtered_df['Customers'].mean():.0f}")
    col3.metric("Avg Conversion", f"{filtered_df['Conversion'].mean():.2f}%")
    col4.metric("Satisfaction", f"{filtered_df['Satisfaction'].mean():.2f}/5")
    
    # KPI Charts using Streamlit's built-in charts
    st.subheader("Revenue Trend")
    st.line_chart(filtered_df.set_index('Date')['Revenue'])
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Customers Over Time")
        st.bar_chart(filtered_df.set_index('Date')['Customers'])
    
    with col2:
        st.subheader("Conversion Rate")
        st.area_chart(filtered_df.set_index('Date')['Conversion'])
    
    # Data table
    st.subheader("KPI Data")
    st.dataframe(filtered_df.style.highlight_max(axis=0))

# Data Analysis Page
elif app_mode == "Data Analysis":
    st.markdown('<p class="big-font">Data Analysis</p>', unsafe_allow_html=True)
    
    # Text inputs
    st.subheader("KPI Configuration")
    kpi_name = st.text_input("KPI Name", "Customer Acquisition Cost")
    target_value = st.number_input("Target Value", value=50.0)
    current_value = st.number_input("Current Value", value=45.6)
    
    # Calculate variance
    variance = current_value - target_value
    variance_pct = (variance / target_value) * 100 if target_value != 0 else 0
    
    st.write(f"**{kpi_name}**")
    st.metric("Variance", f"{variance:.2f}", f"{variance_pct:.2f}%")
    
    # File uploader
    st.subheader("Upload KPI Data")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Uploaded Data:")
        st.dataframe(df.head())
        
        # If numeric columns exist, show basic stats
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            st.subheader("Data Summary")
            st.write(df[numeric_cols].describe())
    
    # Interactive controls
    st.subheader("Simulation Controls")
    simulation_type = st.selectbox("Select Analysis Type", 
                                  ["Trend Analysis", "Variance Report", "Forecast"])
    data_points = st.slider("Number of Data Points", 10, 100, 30)
    
    # Generate sample data for visualization
    x = np.arange(data_points)
    y = np.cumsum(np.random.randn(data_points)) + 100
    
    # Create chart data
    chart_data = pd.DataFrame({
        'x': x,
        'y': y
    })
    
    st.subheader(f"{simulation_type} Results")
    st.line_chart(chart_data.set_index('x'))

# About Page
else:
    st.markdown('<p class="big-font">About SmartKPI</p>', unsafe_allow_html=True)
    
    st.write("""
    ### SmartKPI Dashboard
    
    This application provides a comprehensive dashboard for monitoring 
    key performance indicators with real-time data visualization.
    
    ### Key Features:
    - Interactive KPI monitoring
    - Customizable dashboards
    - Data filtering and analysis
    - Export capabilities
    - Responsive design for all devices
    
    ### Technology Stack:
    - Streamlit for the web framework
    - Pandas for data manipulation
    - NumPy for numerical computations
    
    ### How to Use:
    1. Navigate using the sidebar menu
    2. Apply filters to customize views
    3. Upload your own data for analysis
    4. Configure KPIs based on your needs
    """)

    st.info("Built with ❤️ using [Streamlit](https://streamlit.io)")

# Footer
st.markdown("---")
st.caption("SmartKPI Dashboard • Real-time Performance Monitoring")
import streamlit as st
import pandas as pd
import numpy as np

# Configure page
st.set_page_config(
    page_title="SmartKPI Dashboard",
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
    ["Home", "KPI Dashboard", "Data Analysis", "About"]
)

# Home Page
if app_mode == "Home":
    st.markdown('<p class="big-font">Welcome to SmartKPI Dashboard</p>', unsafe_allow_html=True)
    
    st.write("""
    This is a SmartKPI dashboard application built with Streamlit.
    
    ### Features:
    - Real-time KPI monitoring
    - Interactive data analysis
    - Customizable metrics
    - Responsive design
    """)
    
    st.info("👈 Select a section from the sidebar to get started!")

# KPI Dashboard Page
elif app_mode == "KPI Dashboard":
    st.markdown('<p class="big-font">KPI Dashboard</p>', unsafe_allow_html=True)
    
    # Generate sample data
    @st.cache_data
    def load_kpi_data():
        data = pd.DataFrame({
            'Date': pd.date_range('2023-01-01', periods=50),
            'Revenue': np.random.randint(1000, 5000, 50),
            'Customers': np.random.randint(50, 200, 50),
            'Conversion': np.random.uniform(1.5, 5.0, 50),
            'Satisfaction': np.random.uniform(3.0, 5.0, 50)
        })
        return data
    
    df = load_kpi_data()
    
    # Filters
    st.sidebar.header("Filters")
    date_range = st.sidebar.date_input("Select Date Range", 
                                      [df['Date'].min(), df['Date'].max()])
    
    # Apply filters
    filtered_df = df[
        (df['Date'] >= pd.to_datetime(date_range[0])) & 
        (df['Date'] <= pd.to_datetime(date_range[1]))
    ]
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Revenue", f"${filtered_df['Revenue'].sum():,}")
    col2.metric("Avg Customers", f"{filtered_df['Customers'].mean():.0f}")
    col3.metric("Avg Conversion", f"{filtered_df['Conversion'].mean():.2f}%")
    col4.metric("Satisfaction", f"{filtered_df['Satisfaction'].mean():.2f}/5")
    
    # KPI Charts using Streamlit's built-in charts
    st.subheader("Revenue Trend")
    st.line_chart(filtered_df.set_index('Date')['Revenue'])
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Customers Over Time")
        st.bar_chart(filtered_df.set_index('Date')['Customers'])
    
    with col2:
        st.subheader("Conversion Rate")
        st.area_chart(filtered_df.set_index('Date')['Conversion'])
    
    # Data table
    st.subheader("KPI Data")
    st.dataframe(filtered_df.style.highlight_max(axis=0))

# Data Analysis Page
elif app_mode == "Data Analysis":
    st.markdown('<p class="big-font">Data Analysis</p>', unsafe_allow_html=True)
    
    # Text inputs
    st.subheader("KPI Configuration")
    kpi_name = st.text_input("KPI Name", "Customer Acquisition Cost")
    target_value = st.number_input("Target Value", value=50.0)
    current_value = st.number_input("Current Value", value=45.6)
    
    # Calculate variance
    variance = current_value - target_value
    variance_pct = (variance / target_value) * 100 if target_value != 0 else 0
    
    st.write(f"**{kpi_name}**")
    st.metric("Variance", f"{variance:.2f}", f"{variance_pct:.2f}%")
    
    # File uploader
    st.subheader("Upload KPI Data")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Uploaded Data:")
        st.dataframe(df.head())
        
        # If numeric columns exist, show basic stats
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            st.subheader("Data Summary")
            st.write(df[numeric_cols].describe())
    
    # Interactive controls
    st.subheader("Simulation Controls")
    simulation_type = st.selectbox("Select Analysis Type", 
                                  ["Trend Analysis", "Variance Report", "Forecast"])
    data_points = st.slider("Number of Data Points", 10, 100, 30)
    
    # Generate sample data for visualization
    x = np.arange(data_points)
    y = np.cumsum(np.random.randn(data_points)) + 100
    
    # Create chart data
    chart_data = pd.DataFrame({
        'x': x,
        'y': y
    })
    
    st.subheader(f"{simulation_type} Results")
    st.line_chart(chart_data.set_index('x'))

# About Page
else:
    st.markdown('<p class="big-font">About SmartKPI</p>', unsafe_allow_html=True)
    
    st.write("""
    ### SmartKPI Dashboard
    
    This application provides a comprehensive dashboard for monitoring 
    key performance indicators with real-time data visualization.
    
    ### Key Features:
    - Interactive KPI monitoring
    - Customizable dashboards
    - Data filtering and analysis
    - Export capabilities
    - Responsive design for all devices
    
    ### Technology Stack:
    - Streamlit for the web framework
    - Pandas for data manipulation
    - NumPy for numerical computations
    
    ### How to Use:
    1. Navigate using the sidebar menu
    2. Apply filters to customize views
    3. Upload your own data for analysis
    4. Configure KPIs based on your needs
    """)

    st.info("Built with ❤️ using [Streamlit](https://streamlit.io)")

# Footer
st.markdown("---")
st.caption("SmartKPI Dashboard • Real-time Performance Monitoring")
import streamlit as st
import pandas as pd
import numpy as np

# Configure page
st.set_page_config(
    page_title="SmartKPI Dashboard",
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
    ["Home", "KPI Dashboard", "Data Analysis", "About"]
)

# Home Page
if app_mode == "Home":
    st.markdown('<p class="big-font">Welcome to SmartKPI Dashboard</p>', unsafe_allow_html=True)
    
    st.write("""
    This is a SmartKPI dashboard application built with Streamlit.
    
    ### Features:
    - Real-time KPI monitoring
    - Interactive data analysis
    - Customizable metrics
    - Responsive design
    """)
    
    st.info("👈 Select a section from the sidebar to get started!")

# KPI Dashboard Page
elif app_mode == "KPI Dashboard":
    st.markdown('<p class="big-font">KPI Dashboard</p>', unsafe_allow_html=True)
    
    # Generate sample data
    @st.cache_data
    def load_kpi_data():
        data = pd.DataFrame({
            'Date': pd.date_range('2023-01-01', periods=50),
            'Revenue': np.random.randint(1000, 5000, 50),
            'Customers': np.random.randint(50, 200, 50),
            'Conversion': np.random.uniform(1.5, 5.0, 50),
            'Satisfaction': np.random.uniform(3.0, 5.0, 50)
        })
        return data
    
    df = load_kpi_data()
    
    # Filters
    st.sidebar.header("Filters")
    date_range = st.sidebar.date_input("Select Date Range", 
                                      [df['Date'].min(), df['Date'].max()])
    
    # Apply filters
    filtered_df = df[
        (df['Date'] >= pd.to_datetime(date_range[0])) & 
        (df['Date'] <= pd.to_datetime(date_range[1]))
    ]
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Revenue", f"${filtered_df['Revenue'].sum():,}")
    col2.metric("Avg Customers", f"{filtered_df['Customers'].mean():.0f}")
    col3.metric("Avg Conversion", f"{filtered_df['Conversion'].mean():.2f}%")
    col4.metric("Satisfaction", f"{filtered_df['Satisfaction'].mean():.2f}/5")
    
    # KPI Charts using Streamlit's built-in charts
    st.subheader("Revenue Trend")
    st.line_chart(filtered_df.set_index('Date')['Revenue'])
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Customers Over Time")
        st.bar_chart(filtered_df.set_index('Date')['Customers'])
    
    with col2:
        st.subheader("Conversion Rate")
        st.area_chart(filtered_df.set_index('Date')['Conversion'])
    
    # Data table
    st.subheader("KPI Data")
    st.dataframe(filtered_df.style.highlight_max(axis=0))

# Data Analysis Page
elif app_mode == "Data Analysis":
    st.markdown('<p class="big-font">Data Analysis</p>', unsafe_allow_html=True)
    
    # Text inputs
    st.subheader("KPI Configuration")
    kpi_name = st.text_input("KPI Name", "Customer Acquisition Cost")
    target_value = st.number_input("Target Value", value=50.0)
    current_value = st.number_input("Current Value", value=45.6)
    
    # Calculate variance
    variance = current_value - target_value
    variance_pct = (variance / target_value) * 100 if target_value != 0 else 0
    
    st.write(f"**{kpi_name}**")
    st.metric("Variance", f"{variance:.2f}", f"{variance_pct:.2f}%")
    
    # File uploader
    st.subheader("Upload KPI Data")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Uploaded Data:")
        st.dataframe(df.head())
        
        # If numeric columns exist, show basic stats
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            st.subheader("Data Summary")
            st.write(df[numeric_cols].describe())
    
    # Interactive controls
    st.subheader("Simulation Controls")
    simulation_type = st.selectbox("Select Analysis Type", 
                                  ["Trend Analysis", "Variance Report", "Forecast"])
    data_points = st.slider("Number of Data Points", 10, 100, 30)
    
    # Generate sample data for visualization
    x = np.arange(data_points)
    y = np.cumsum(np.random.randn(data_points)) + 100
    
    # Create chart data
    chart_data = pd.DataFrame({
        'x': x,
        'y': y
    })
    
    st.subheader(f"{simulation_type} Results")
    st.line_chart(chart_data.set_index('x'))

# About Page
else:
    st.markdown('<p class="big-font">About SmartKPI</p>', unsafe_allow_html=True)
    
    st.write("""
    ### SmartKPI Dashboard
    
    This application provides a comprehensive dashboard for monitoring 
    key performance indicators with real-time data visualization.
    
    ### Key Features:
    - Interactive KPI monitoring
    - Customizable dashboards
    - Data filtering and analysis
    - Export capabilities
    - Responsive design for all devices
    
    ### Technology Stack:
    - Streamlit for the web framework
    - Pandas for data manipulation
    - NumPy for numerical computations
    
    ### How to Use:
    1. Navigate using the sidebar menu
    2. Apply filters to customize views
    3. Upload your own data for analysis
    4. Configure KPIs based on your needs
    """)

    st.info("Built with ❤️ using [Streamlit](https://streamlit.io)")

# Footer
st.markdown("---")
st.caption("SmartKPI Dashboard • Real-time Performance Monitoring")
import streamlit as st
import pandas as pd
import numpy as np

# Configure page
st.set_page_config(
    page_title="SmartKPI Dashboard",
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
    ["Home", "KPI Dashboard", "Data Analysis", "About"]
)

# Home Page
if app_mode == "Home":
    st.markdown('<p class="big-font">Welcome to SmartKPI Dashboard</p>', unsafe_allow_html=True)
    
    st.write("""
    This is a SmartKPI dashboard application built with Streamlit.
    
    ### Features:
    - Real-time KPI monitoring
    - Interactive data analysis
    - Customizable metrics
    - Responsive design
    """)
    
    st.info("👈 Select a section from the sidebar to get started!")

# KPI Dashboard Page
elif app_mode == "KPI Dashboard":
    st.markdown('<p class="big-font">KPI Dashboard</p>', unsafe_allow_html=True)
    
    # Generate sample data
    @st.cache_data
    def load_kpi_data():
        data = pd.DataFrame({
            'Date': pd.date_range('2023-01-01', periods=50),
            'Revenue': np.random.randint(1000, 5000, 50),
            'Customers': np.random.randint(50, 200, 50),
            'Conversion': np.random.uniform(1.5, 5.0, 50),
            'Satisfaction': np.random.uniform(3.0, 5.0, 50)
        })
        return data
    
    df = load_kpi_data()
    
    # Filters
    st.sidebar.header("Filters")
    date_range = st.sidebar.date_input("Select Date Range", 
                                      [df['Date'].min(), df['Date'].max()])
    
    # Apply filters
    filtered_df = df[
        (df['Date'] >= pd.to_datetime(date_range[0])) & 
        (df['Date'] <= pd.to_datetime(date_range[1]))
    ]
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Revenue", f"${filtered_df['Revenue'].sum():,}")
    col2.metric("Avg Customers", f"{filtered_df['Customers'].mean():.0f}")
    col3.metric("Avg Conversion", f"{filtered_df['Conversion'].mean():.2f}%")
    col4.metric("Satisfaction", f"{filtered_df['Satisfaction'].mean():.2f}/5")
    
    # KPI Charts using Streamlit's built-in charts
    st.subheader("Revenue Trend")
    st.line_chart(filtered_df.set_index('Date')['Revenue'])
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Customers Over Time")
        st.bar_chart(filtered_df.set_index('Date')['Customers'])
    
    with col2:
        st.subheader("Conversion Rate")
        st.area_chart(filtered_df.set_index('Date')['Conversion'])
    
    # Data table
    st.subheader("KPI Data")
    st.dataframe(filtered_df.style.highlight_max(axis=0))

# Data Analysis Page
elif app_mode == "Data Analysis":
    st.markdown('<p class="big-font">Data Analysis</p>', unsafe_allow_html=True)
    
    # Text inputs
    st.subheader("KPI Configuration")
    kpi_name = st.text_input("KPI Name", "Customer Acquisition Cost")
    target_value = st.number_input("Target Value", value=50.0)
    current_value = st.number_input("Current Value", value=45.6)
    
    # Calculate variance
    variance = current_value - target_value
    variance_pct = (variance / target_value) * 100 if target_value != 0 else 0
    
    st.write(f"**{kpi_name}**")
    st.metric("Variance", f"{variance:.2f}", f"{variance_pct:.2f}%")
    
    # File uploader
    st.subheader("Upload KPI Data")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Uploaded Data:")
        st.dataframe(df.head())
        
        # If numeric columns exist, show basic stats
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            st.subheader("Data Summary")
            st.write(df[numeric_cols].describe())
    
    # Interactive controls
    st.subheader("Simulation Controls")
    simulation_type = st.selectbox("Select Analysis Type", 
                                  ["Trend Analysis", "Variance Report", "Forecast"])
    data_points = st.slider("Number of Data Points", 10, 100, 30)
    
    # Generate sample data for visualization
    x = np.arange(data_points)
    y = np.cumsum(np.random.randn(data_points)) + 100
    
    # Create chart data
    chart_data = pd.DataFrame({
        'x': x,
        'y': y
    })
    
    st.subheader(f"{simulation_type} Results")
    st.line_chart(chart_data.set_index('x'))

# About Page
else:
    st.markdown('<p class="big-font">About SmartKPI</p>', unsafe_allow_html=True)
    
    st.write("""
    ### SmartKPI Dashboard
    
    This application provides a comprehensive dashboard for monitoring 
    key performance indicators with real-time data visualization.
    
    ### Key Features:
    - Interactive KPI monitoring
    - Customizable dashboards
    - Data filtering and analysis
    - Export capabilities
    - Responsive design for all devices
    
    ### Technology Stack:
    - Streamlit for the web framework
    - Pandas for data manipulation
    - NumPy for numerical computations
    
    ### How to Use:
    1. Navigate using the sidebar menu
    2. Apply filters to customize views
    3. Upload your own data for analysis
    4. Configure KPIs based on your needs
    """)

    st.info("Built with ❤️ using [Streamlit](https://streamlit.io)")

# Footer
st.markdown("---")
st.caption("SmartKPI Dashboard • Real-time Performance Monitoring")
import streamlit as st
import pandas as pd
import numpy as np

# Configure page
st.set_page_config(
    page_title="SmartKPI Dashboard",
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
    ["Home", "KPI Dashboard", "Data Analysis", "About"]
)

# Home Page
if app_mode == "Home":
    st.markdown('<p class="big-font">Welcome to SmartKPI Dashboard</p>', unsafe_allow_html=True)
    
    st.write("""
    This is a SmartKPI dashboard application built with Streamlit.
    
    ### Features:
    - Real-time KPI monitoring
    - Interactive data analysis
    - Customizable metrics
    - Responsive design
    """)
    
    st.info("👈 Select a section from the sidebar to get started!")

# KPI Dashboard Page
elif app_mode == "KPI Dashboard":
    st.markdown('<p class="big-font">KPI Dashboard</p>', unsafe_allow_html=True)
    
    # Generate sample data
    @st.cache_data
    def load_kpi_data():
        data = pd.DataFrame({
            'Date': pd.date_range('2023-01-01', periods=50),
            'Revenue': np.random.randint(1000, 5000, 50),
            'Customers': np.random.randint(50, 200, 50),
            'Conversion': np.random.uniform(1.5, 5.0, 50),
            'Satisfaction': np.random.uniform(3.0, 5.0, 50)
        })
        return data
    
    df = load_kpi_data()
    
    # Filters
    st.sidebar.header("Filters")
    date_range = st.sidebar.date_input("Select Date Range", 
                                      [df['Date'].min(), df['Date'].max()])
    
    # Apply filters
    filtered_df = df[
        (df['Date'] >= pd.to_datetime(date_range[0])) & 
        (df['Date'] <= pd.to_datetime(date_range[1]))
    ]
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Revenue", f"${filtered_df['Revenue'].sum():,}")
    col2.metric("Avg Customers", f"{filtered_df['Customers'].mean():.0f}")
    col3.metric("Avg Conversion", f"{filtered_df['Conversion'].mean():.2f}%")
    col4.metric("Satisfaction", f"{filtered_df['Satisfaction'].mean():.2f}/5")
    
    # KPI Charts using Streamlit's built-in charts
    st.subheader("Revenue Trend")
    st.line_chart(filtered_df.set_index('Date')['Revenue'])
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Customers Over Time")
        st.bar_chart(filtered_df.set_index('Date')['Customers'])
    
    with col2:
        st.subheader("Conversion Rate")
        st.area_chart(filtered_df.set_index('Date')['Conversion'])
    
    # Data table
    st.subheader("KPI Data")
    st.dataframe(filtered_df.style.highlight_max(axis=0))

# Data Analysis Page
elif app_mode == "Data Analysis":
    st.markdown('<p class="big-font">Data Analysis</p>', unsafe_allow_html=True)
    
    # Text inputs
    st.subheader("KPI Configuration")
    kpi_name = st.text_input("KPI Name", "Customer Acquisition Cost")
    target_value = st.number_input("Target Value", value=50.0)
    current_value = st.number_input("Current Value", value=45.6)
    
    # Calculate variance
    variance = current_value - target_value
    variance_pct = (variance / target_value) * 100 if target_value != 0 else 0
    
    st.write(f"**{kpi_name}**")
    st.metric("Variance", f"{variance:.2f}", f"{variance_pct:.2f}%")
    
    # File uploader
    st.subheader("Upload KPI Data")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Uploaded Data:")
        st.dataframe(df.head())
        
        # If numeric columns exist, show basic stats
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            st.subheader("Data Summary")
            st.write(df[numeric_cols].describe())
    
    # Interactive controls
    st.subheader("Simulation Controls")
    simulation_type = st.selectbox("Select Analysis Type", 
                                  ["Trend Analysis", "Variance Report", "Forecast"])
    data_points = st.slider("Number of Data Points", 10, 100, 30)
    
    # Generate sample data for visualization
    x = np.arange(data_points)
    y = np.cumsum(np.random.randn(data_points)) + 100
    
    # Create chart data
    chart_data = pd.DataFrame({
        'x': x,
        'y': y
    })
    
    st.subheader(f"{simulation_type} Results")
    st.line_chart(chart_data.set_index('x'))

# About Page
else:
    st.markdown('<p class="big-font">About SmartKPI</p>', unsafe_allow_html=True)
    
    st.write("""
    ### SmartKPI Dashboard
    
    This application provides a comprehensive dashboard for monitoring 
    key performance indicators with real-time data visualization.
    
    ### Key Features:
    - Interactive KPI monitoring
    - Customizable dashboards
    - Data filtering and analysis
    - Export capabilities
    - Responsive design for all devices
    
    ### Technology Stack:
    - Streamlit for the web framework
    - Pandas for data manipulation
    - NumPy for numerical computations
    
    ### How to Use:
    1. Navigate using the sidebar menu
    2. Apply filters to customize views
    3. Upload your own data for analysis
    4. Configure KPIs based on your needs
    """)

    st.info("Built with ❤️ using [Streamlit](https://streamlit.io)")

# Footer
st.markdown("---")
st.caption("SmartKPI Dashboard • Real-time Performance Monitoring")
import streamlit as st
import pandas as pd
import numpy as np

# Configure page
st.set_page_config(
    page_title="SmartKPI Dashboard",
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
    ["Home", "KPI Dashboard", "Data Analysis", "About"]
)

# Home Page
if app_mode == "Home":
    st.markdown('<p class="big-font">Welcome to SmartKPI Dashboard</p>', unsafe_allow_html=True)
    
    st.write("""
    This is a SmartKPI dashboard application built with Streamlit.
    
    ### Features:
    - Real-time KPI monitoring
    - Interactive data analysis
    - Customizable metrics
    - Responsive design
    """)
    
    st.info("👈 Select a section from the sidebar to get started!")

# KPI Dashboard Page
elif app_mode == "KPI Dashboard":
    st.markdown('<p class="big-font">KPI Dashboard</p>', unsafe_allow_html=True)
    
    # Generate sample data
    @st.cache_data
    def load_kpi_data():
        data = pd.DataFrame({
            'Date': pd.date_range('2023-01-01', periods=50),
            'Revenue': np.random.randint(1000, 5000, 50),
            'Customers': np.random.randint(50, 200, 50),
            'Conversion': np.random.uniform(1.5, 5.0, 50),
            'Satisfaction': np.random.uniform(3.0, 5.0, 50)
        })
        return data
    
    df = load_kpi_data()
    
    # Filters
    st.sidebar.header("Filters")
    date_range = st.sidebar.date_input("Select Date Range", 
                                      [df['Date'].min(), df['Date'].max()])
    
    # Apply filters
    filtered_df = df[
        (df['Date'] >= pd.to_datetime(date_range[0])) & 
        (df['Date'] <= pd.to_datetime(date_range[1]))
    ]
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Revenue", f"${filtered_df['Revenue'].sum():,}")
    col2.metric("Avg Customers", f"{filtered_df['Customers'].mean():.0f}")
    col3.metric("Avg Conversion", f"{filtered_df['Conversion'].mean():.2f}%")
    col4.metric("Satisfaction", f"{filtered_df['Satisfaction'].mean():.2f}/5")
    
    # KPI Charts using Streamlit's built-in charts
    st.subheader("Revenue Trend")
    st.line_chart(filtered_df.set_index('Date')['Revenue'])
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Customers Over Time")
        st.bar_chart(filtered_df.set_index('Date')['Customers'])
    
    with col2:
        st.subheader("Conversion Rate")
        st.area_chart(filtered_df.set_index('Date')['Conversion'])
    
    # Data table
    st.subheader("KPI Data")
    st.dataframe(filtered_df.style.highlight_max(axis=0))

# Data Analysis Page
elif app_mode == "Data Analysis":
    st.markdown('<p class="big-font">Data Analysis</p>', unsafe_allow_html=True)
    
    # Text inputs
    st.subheader("KPI Configuration")
    kpi_name = st.text_input("KPI Name", "Customer Acquisition Cost")
    target_value = st.number_input("Target Value", value=50.0)
    current_value = st.number_input("Current Value", value=45.6)
    
    # Calculate variance
    variance = current_value - target_value
    variance_pct = (variance / target_value) * 100 if target_value != 0 else 0
    
    st.write(f"**{kpi_name}**")
    st.metric("Variance", f"{variance:.2f}", f"{variance_pct:.2f}%")
    
    # File uploader
    st.subheader("Upload KPI Data")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Uploaded Data:")
        st.dataframe(df.head())
        
        # If numeric columns exist, show basic stats
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            st.subheader("Data Summary")
            st.write(df[numeric_cols].describe())
    
    # Interactive controls
    st.subheader("Simulation Controls")
    simulation_type = st.selectbox("Select Analysis Type", 
                                  ["Trend Analysis", "Variance Report", "Forecast"])
    data_points = st.slider("Number of Data Points", 10, 100, 30)
    
    # Generate sample data for visualization
    x = np.arange(data_points)
    y = np.cumsum(np.random.randn(data_points)) + 100
    
    # Create chart data
    chart_data = pd.DataFrame({
        'x': x,
        'y': y
    })
    
    st.subheader(f"{simulation_type} Results")
    st.line_chart(chart_data.set_index('x'))

# About Page
else:
    st.markdown('<p class="big-font">About SmartKPI</p>', unsafe_allow_html=True)
    
    st.write("""
    ### SmartKPI Dashboard
    
    This application provides a comprehensive dashboard for monitoring 
    key performance indicators with real-time data visualization.
    
    ### Key Features:
    - Interactive KPI monitoring
    - Customizable dashboards
    - Data filtering and analysis
    - Export capabilities
    - Responsive design for all devices
    
    ### Technology Stack:
    - Streamlit for the web framework
    - Pandas for data manipulation
    - NumPy for numerical computations
    
    ### How to Use:
    1. Navigate using the sidebar menu
    2. Apply filters to customize views
    3. Upload your own data for analysis
    4. Configure KPIs based on your needs
    """)

    st.info("Built with ❤️ using [Streamlit](https://streamlit.io)")

# Footer
st.markdown("---")
st.caption("SmartKPI Dashboard • Real-time Performance Monitoring")
