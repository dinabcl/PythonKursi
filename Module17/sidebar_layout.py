import streamlit as st

st.sidebar.header("Sidebar")
st.sidebar.write("This is the sidebar")
st.sidebar.selectbox("Chosse an option", ["Optiion 1","Optiion 2","Optiion 3"])
st.sidebar.radio("Go to", ["Home","Data","Settings"])