import streamlit as st
import os

st.write(st.secrets["test"])

result = os.environ.get("test", default_value)

st.write( result)