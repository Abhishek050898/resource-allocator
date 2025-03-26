import streamlit as st

st.title("📊 Project Analytics")

# Embed Power BI Dashboard
st.markdown("""
<iframe title="Power BI Report" width="100%" height="600"
src="https://app.powerbi.com/view?r=eyJrIjoiYTQzYmM3MzYtYWM2NC00Y2Q3LWIwMjktODU2YjJmMTZmOTk2IiwidCI6ImZiZjdlMDJmLWU5NGEtNGRmMi1hMGE5LTllMzBmNGQ1Y2Q2NSJ9"
frameborder="0" allowFullScreen="true"></iframe>
""", unsafe_allow_html=True)


