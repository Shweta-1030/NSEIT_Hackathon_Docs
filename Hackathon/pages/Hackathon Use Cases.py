import streamlit as st
import pandas as pd
#from IPython.display import display, HTML

st.set_page_config(layout="wide")

##st.markdown("(AI)<sup>5</sup>", unsafe_allow_html=True)
st.title("List of Use Cases")
##st.markdown("<h1 style='text-align: center; color: grey;'>Big headline</h1>", unsafe_allow_html=True)

df = pd.read_csv("data/hackathon_use_cases.csv")

#display(HTML(df.to_html(index=False)))
#df = st.dataframe(df,hide_index=True)
#df = df.style.hide(axis="index")
df = st.dataframe(df,hide_index=True)
#st.write(df.to_html(), unsafe_allow_html=True)

#st.table(df)
#st.write(df)
