import pandas as pd
import streamlit as st

st.header("Displaying dataframes")

data = pd.DataFrame({
    'Name': ['Alice', 'Varka', 'Columbina'],
    'Age': [500, 37, 1000],
    'City': ['Monstadt', 'Monstadt', 'Nod-Krai']
})

st.dataframe(data)