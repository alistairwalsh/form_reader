import streamlit as st
from pdf2image import convert_from_path, convert_from_bytes
from PIL import Image
import pytesseract



uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
st.write(uploaded_file)

if uploaded_file is not None:
        images = convert_from_bytes(uploaded_file.read())
        for page in images:
            st.image(page, use_column_width=True)
            data = pytesseract.image_to_data(page) #, output_type=Output.DICT


# def extract_data(feed):
#     data = []
#     with pdfplumber.load(feed) as pdf:
#         pages = pdf.pages
#         for p in pages:
#             data.append(p.extract_tables())
#     return None # build more code to return a dataframe 