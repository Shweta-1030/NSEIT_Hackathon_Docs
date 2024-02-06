import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

##st.markdown("(AI)<sup>5</sup>", unsafe_allow_html=True)

st.title("List of Use Cases")
##st.markdown("<h1 style='text-align: center; color: grey;'>Big headline</h1>", unsafe_allow_html=True)

df = pd.read_csv("data/hackathon_use_cases.csv")

#st.table(df)
st.write(df)