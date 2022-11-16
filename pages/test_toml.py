import streamlit as st
import os

default_value = 'not found'
st.write(st.secrets["test"])

result = os.environ.get("test", default_value)

st.write( result)