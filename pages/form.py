import streamlit as st
from pdf2image import convert_from_path, convert_from_bytes
from PIL import Image
import pytesseract
from pytesseract import Output
import cv2



uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
st.write(uploaded_file)

if uploaded_file is not None:
        images = convert_from_bytes(uploaded_file.read())
        for page in images:
            st.image(page, use_column_width=True)
            data = pytesseract.image_to_data(page, output_type=Output.DICT)
            keys = list(data.keys())
            st.write(keys)
            #st.write(data['text'])
            st.write(data["block_num"][0][0])
            break
