import streamlit as st

st.title("Echo Bot")

with st.chat_message("user"):
    st.write("Hello 👋")