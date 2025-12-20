import streamlit as st

tab1,tab2,tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.header("Content for Tab1")
    st.write("This is content for the first tab")

with tab2:
    st.header("Content for Tab2")
    st.write("This is content for the second tab")

with tab3:
    st.header("Content for Tab3")
    st.write("This is content for the third tab")
