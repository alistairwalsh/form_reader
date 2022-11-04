import streamlit as st
from pdf2image import convert_from_path, convert_from_bytes

uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
st.write(uploaded_file)
# if uploaded_file is not None:
#         images = convert_from_bytes(uploaded_file.read())


# def extract_data(feed):
#     data = []
#     with pdfplumber.load(feed) as pdf:
#         pages = pdf.pages
#         for p in pages:
#             data.append(p.extract_tables())
#     return None # build more code to return a dataframe 