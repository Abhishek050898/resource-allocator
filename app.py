import streamlit as st
import os

# Set the page title and layout
st.set_page_config(
    page_title="Resource Planning Tool",
    page_icon="🧑‍💼",
    layout="wide"
)

st.image("assets/logo.png", caption="Resource Planning Tool", use_container_width=True)


# Add an introductory message
st.title("Welcome to the Resource Planning and Analysis Tool!")
st.markdown("""
This tool is designed to help you streamline resource planning, allocation, 
and project analysis with ease. Navigate through the sections using the sidebar!
""")

# Sidebar Navigation
# st.sidebar.title("Navigation")

# Example navigation logic (commented code for illustration purposes)
# page = st.sidebar.radio("Go to", ["Home", "Form", "Analytics"])

# # Load the appropriate page based on user selection
# if page == "Home":
#     from pages import 1_Home
#     1_Home.show()

# elif page == "Form":
#     from pages import 2_Predictive_Resource_Allocator
#     2_Predictive_Resource_Allocator.main()

# elif page == "Analytics":
#     from pages import 3_Analytics_Dashboard
#     3_Analytics_Dashboard.show()
