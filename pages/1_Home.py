import streamlit as st

def show():
    st.title("🏗️ Resource Allocation & Planning Tool for Construction Projects")
    st.markdown("---")

    st.write("""
    Welcome to the **Dynamic Resource Allocation & Planning Tool**. This application helps construction projects
    efficiently **predict workforce requirements**, **optimize project planning** and *optimize cost strategies**.

    ### **🌟 Features**
    - 📊 Predict **Department Count & Names**
    - 👥 Estimate **Total Number of Employees to be assigned to bidding projects and Employees per department.**
    - 🔍 View **Detailed Analytics on Historical Workforce Timesheet data and Client Orders data in Power BI**
    - 🔍 View **Predictive Analytics for Operational Team and Project Planners involved in decision making**

    Navigate using the **sidebar menu** to explore different features.
    """)

if __name__ == "__main__":
    show()
