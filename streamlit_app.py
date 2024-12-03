import streamlit as st
from datetime import datetime
import pandas as pd
import streamlit as st

import plotly.express as px
import numpy as np
import os

st.set_page_config(layout='wide')


st.markdown("""
<style>
.st-emotion-cache-rci5h9 {
    display: inline-flex
;
    -webkit-box-align: center;
    border: none !important;
    background: transparent;
    align-items: center;
    -webkit-box-pack: center;
    justify-content: center;
    font-weight: 400;
    padding: 0.25rem 0.75rem;
    border-radius: 0.5rem;
    min-height: 2.5rem;
    margin: 0px;
    line-height: 1.6;
    color: inherit;
    width: auto;
    cursor: pointer;
    user-select: none;
    /* background-color: rgb(43, 44, 54); */
    border: 1px solid rgba(250, 250, 250, 0.2);}
            
            .st-emotion-cache-13na8ym {
    margin-bottom: 0px;
    margin-top: 0px;
    width: 100%;
    border-style: solid;
    border-width: 1px;
    /* border-color: rgba(250, 250, 250, 0.2); */
    /* border-radius: 0.5rem; */
    border: none;
}
            
        summary.st-emotion-cache-17sglzk.eqpbllx1:hover {
            background-color:gray;
            border-radius:5px;
            font-size: 200px;
}


            



















                .streamlit-expanderHeader {
        font-size: 50px; /* Change this to your desired font size */
        font-weight: bold; /* Optional: Make the text bold */
        color: #4CAF50; /* Optional: Customize the text color */
    }

            .st-emotion-cache-ysk9xe p {
    word-break: break-word;
    margin-bottom: 0px;
    font-size: 18px;
}








.st-emotion-cache-16oe73j {
    margin-bottom: 0px;
    margin-top: 0px;
    width: 100%;
  
   
    border: none !important;
}

.st-emotion-cache-ior94r {
    display: inline-flex
;
    -webkit-box-align: center;
    align-items: center;
    -webkit-box-pack: center;
    justify-content: center;
    font-weight: 400;
    padding: 0.25rem 0.75rem;
    border-radius: 0.5rem;
    min-height: 2.5rem;
    margin: 0px;
    line-height: 1.6;
    color: inherit;
    width: auto;
    cursor: pointer;
    user-select: none;
   
    border: none !important;
            background: transparent;
}
            
            button.st-emotion-cache-18hpnz2.ef3psqc19 {
    border: none;
    background: transparent;
}
            
            button.st-emotion-cache-18hpnz2.ef3psqc19 {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-weight: 400;
    padding: 0.25rem 0.75rem;
    border-radius: 0.5rem;
    min-height: 2.5rem;
    margin: 0px;
    line-height: 1.6;
    color: inherit;
    width: auto;
    cursor: pointer;
    user-select: none;
    border: none !important;
    background: transparent; /* Initial background */
    transition: background 0.3s ease; /* Smooth transition for background */
}
/* Hover effect: Change background and add slight scale */
button.st-emotion-cache-18hpnz2.ef3psqc19:hover {
    background: rgba(54, 117, 175, 0.3); /* Change background on hover */
    transform: scale(1.05); /* Slight scale effect on hover */
}


            
            .st-emotion-cache-1dn3z2w {
    position: fixed;
    top: 0px;
    left: 0px;
    right: 0px;
    height: 5rem;
    background: rgb(0 0 0);
    outline: none;
    z-index: 999990;
    display: block;
}
            









            
</style>



""", unsafe_allow_html=True)








st.logo(r'assets\logo.svg', icon_image='assets\logo-sm.svg',size='large')


if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

# Define page content functions
def home():


    st.header('this is header')
def price_and_fundamental():
    # st.header(st.get_option(theme.primaryColor))
    st.header('Price and Fundamentals')

    # Generate data dynamically for filters
    if "data" not in st.session_state:
        np.random.seed(42)  # For reproducible random data
        dates = pd.date_range(start='2024-01-01', end='2024-08-31', freq='D')
        jobs = ['Job_A', 'Job_B', 'Job_C', 'Job_D']
        scenarios = ['Scenario_A', 'Scenario_B', 'Scenario_C']
        areas = ['TKO', 'SYS', 'HKD', 'CHB', 'HKR', 'KNS', 'CGK']

        # Create a DataFrame with all combinations of Jobs, Scenarios, and Areas
        data = pd.DataFrame({
            'Date': np.random.choice(dates, 1000),
            'Job': np.random.choice(jobs, 1000),
            'Scenario': np.random.choice(scenarios, 1000),
            'Area': np.random.choice(areas, 1000),
            'Value': np.random.randint(100, 1000, 1000)  # Random values
        })
        st.session_state.data = data

    data = st.session_state.data



    # Ensure Date column is in datetime.date format for compatibility
    data['Date'] = pd.to_datetime(data['Date']).dt.date

    col1, col2 = st.columns(2)

    st.header('Select Data')
    st.write('Use the widget below to explore the generation model')

    # Left Column Filters
    with col1:
        col1_1, col1_2, col1_3 = st.columns(3)
        with col1_1:
            selected_job = st.selectbox(
                'Select a job',
                sorted(data['Job'].unique())  # Populate based on available data
            )
            compare_jobs = st.checkbox('Compare two jobs', help='Compare jobs here')
        with col1_2:
            selected_scenario = st.selectbox(
                'Select Scenario',
                sorted(data['Scenario'].unique())  # Populate based on available data
            )
            select_all_areas = st.checkbox('Select all areas', help='Select all areas here')
            st.button('Load Data')
        with col1_3:
                
            selected_granularity = st.selectbox(
                'Select granularity',
                ['Daily', 'Weekly', 'Monthly', 'Quarterly', 'Yearly']
            )
            show_inputs_only = st.checkbox(
                'Show inputs only',
                help="Check to show only the inputs for the run. Useful if the run hasn't been solved and inserted yet.",
                key="Show_inputs_only"
            )
            
            if st.button('Refresh job list'):
                st.experimental_rerun()


        col1_col1, col1_col2, col1_col3 = st.columns(3)

        with col1_col1:
            pass
            # compare_jobs = st.checkbox('Compare two jobs', help='Compare jobs here')
        with col1_col2:
            pass
            # select_all_areas = st.checkbox('Select all areas', help='Select all areas here')
            # st.button('Load Data')
        with col1_col3:
            pass
            # show_inputs_only = st.checkbox(
            #     'Show inputs only',
            #     help="Check to show only the inputs for the run. Useful if the run hasn't been solved and inserted yet.",
            #     key="Show_inputs_only"
            # )
            
            # if st.button('Refresh job list'):
            #     st.experimental_rerun()
            
            

    # Right Column Filters
    with col2:
        if select_all_areas:
            selected_areas = data['Area'].unique().tolist()
        else:
            selected_areas = st.multiselect(
                'Select areas',
                sorted(data['Area'].unique()),  # Populate based on available data
                default=['TKO']
            )

        # selected_granularity = st.selectbox(
        #     'Select granularity',
        #     ['Daily', 'Weekly', 'Monthly', 'Quarterly', 'Yearly']
        # )

        selected_date_range = st.slider(
            'Select date range',
            min_value=data['Date'].min(),
            max_value=data['Date'].max(),
            value=(data['Date'].min(), data['Date'].max()),
            format="YYYY-MM-DD", key='this'
        )



    # Filter data
    filtered_data = data[
        (data['Job'] == selected_job) &
        (data['Scenario'] == selected_scenario) &
        (data['Area'].isin(selected_areas)) &
        (data['Date'] >= selected_date_range[0]) &
        (data['Date'] <= selected_date_range[1])
    ]

    # Aggregate data based on selected granularity
    if not filtered_data.empty:
        if selected_granularity != 'Daily':
            filtered_data['Date'] = pd.to_datetime(filtered_data['Date'])

            if selected_granularity == 'Weekly':
                filtered_data['Date'] = filtered_data['Date'].dt.to_period('W').apply(lambda r: r.start_time)
            elif selected_granularity == 'Monthly':
                filtered_data['Date'] = filtered_data['Date'].dt.to_period('M').apply(lambda r: r.start_time)
            elif selected_granularity == 'Quarterly':
                filtered_data['Date'] = filtered_data['Date'].dt.to_period('Q').apply(lambda r: r.start_time)
            elif selected_granularity == 'Yearly':
                filtered_data['Date'] = filtered_data['Date'].dt.to_period('Y').apply(lambda r: r.start_time)

            # Aggregate by mean Value for the granularity
            filtered_data = filtered_data.groupby(['Date', 'Area'], as_index=False)['Value'].mean()



        # Plot with Plotly
    st.subheader('Interactive Plot')
    if not filtered_data.empty:
        fig = px.line(
            filtered_data,
            x='Date',
            y='Value',
            color='Area',
            title=f'Filtered Data Over Time ({selected_granularity})'
        )

        # Update layout to customize background and text color
        fig.update_layout(
            plot_bgcolor='rgb(30,30,30)',  # Dark gray for the plot area
            paper_bgcolor='rgb(20,20,20)',  # Darker gray for the outer area
            font=dict(
                color='white',  # White font color for all text
                size=14,        # Global font size
            ),
            title=dict(
                text=f'Filtered Data Over Time ({selected_granularity})',
                font=dict(
                    size=20,
                    color='white'
                )
            ),
            xaxis=dict(
                showgrid=False,
                color='white',  # White x-axis labels
                title=dict(
                    text='Date',
                    font=dict(color='white')  # X-axis title color
                )
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor='gray',  # Gray gridlines
                color='white',  # White y-axis labels
                title=dict(
                    text='Value',
                    font=dict(color='white')  # Y-axis title color
                )
            ),
            legend=dict(
                title=dict(text='Area', font=dict(color='white')),  # Legend title color
                font=dict(color='white')  # Legend items color
            )
        )

        st.plotly_chart(fig, use_container_width=True)


        st.subheader('Original Data')
        st.dataframe(data, use_container_width=True)
        st.header('Filtered dataframe')
        if not filtered_data.empty:
            st.dataframe(filtered_data, use_container_width=True)
        
    else:
        st.write("No data available for the selected filters.")
    
def generation():
    st.title("🏭 Generation")
    st.write("Details about generation.")

def load_factors():
    st.title("🌩️ Load Factors")
    st.write("Details about load factors.")

def calendar_creation():
    st.title("📆 Calendar Creation")
    st.write("Create and manage calendars.")

def calibration():
    st.title("🔌 Calibration")
    st.write("Calibrate your models.")

def weather_paths():
    st.title("🌦️ Weather Paths")
    st.write("Weather-related data.")

def app_page():
    st.title("📊 PyGWalker Integration")
    st.write("Interactive visualizations with PyGWalker.")

# # Sidebar menu with expanders
with st.sidebar:
    
    
    if st.button("🏚️ Home"):
            st.session_state.current_page = "home"
            

    with st.expander(" Generation Model"):
        if st.button("🗾Price & Fun"):
            st.session_state.current_page = "price_and_fundamental"


        if st.button("🏭 Generation"):
            st.session_state.current_page = "generation"
        if st.button("🌩️ Load Factors"):
            st.session_state.current_page = "load_factors"

    with st.expander("Load Scenarios"):
        if st.button("📆 Calendar Creation"):
            st.session_state.current_page = "calendar_creation"
        if st.button("🔌 Calibration"):
            st.session_state.current_page = "calibration"
        if st.button("🌦️ Weather Paths"):
            st.session_state.current_page = "weather_paths"

    with st.expander("Commodities Scenarios"):
        if st.button("📊 PyGWalker", key='rajratan'):
            st.session_state.current_page = "app_page"

# Render the selected page
if st.session_state.current_page == "home":
    home()
elif st.session_state.current_page == "price_and_fundamental":
    price_and_fundamental()
elif st.session_state.current_page == "generation":
    generation()
elif st.session_state.current_page == "load_factors":
    load_factors()
elif st.session_state.current_page == "calendar_creation":
    calendar_creation()
elif st.session_state.current_page == "calibration":
    calibration()
elif st.session_state.current_page == "weather_paths":
    weather_paths()
elif st.session_state.current_page == "app_page":
    app_page()


