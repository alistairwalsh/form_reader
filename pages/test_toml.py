import streamlit as st
import os

st.write(st.secrets["test"])


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = st.secrets["test"]

st.write(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])