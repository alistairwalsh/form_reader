import streamlit as st
import os

st.write(st.secrets["test"])

result = os.environ["test"]

st.write( result)