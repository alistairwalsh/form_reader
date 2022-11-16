import streamlit as st
import os

default_value = 'not found'
st.write(st.secrets["GOOGLE_APPLICATION_CREDENTIALS"]["type"])

result = os.environ.get("TEST", default_value)

st.write( result)