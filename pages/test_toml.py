import streamlit as st
import os

default_value = 'not found'
st.write(st.secrets["GOOGLE_APPLICATION_CREDENTIALS"]["type"])

result = os.environ["GOOGLE_APPLICATION_CREDENTIALS"]["type"]

st.write( result)