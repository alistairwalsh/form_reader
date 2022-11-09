import pandas as pd
import streamlit as st
from pdf2image import convert_from_path, convert_from_bytes
from PIL import Image
import pytesseract
from pytesseract import Output
import cv2
import numpy as np


uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
st.write(uploaded_file)

if uploaded_file is not None:
        images = convert_from_bytes(uploaded_file.read())
        for page in images:
            opencv_image = np.array(page)
            st.image(page, use_column_width=True)
            
            data = pytesseract.image_to_data(page, output_type=Output.DATAFRAME)
            st.dataframe(data)
            rehab = data.loc[26,['left','top','width','height','text']]
            #(x, y), (x + w, y + h)
            st.write(rehab)
            cv2.rectangle(opencv_image, (rehab['left'], rehab['top']), (rehab['left'] + rehab['width'], rehab['top'] + rehab['height']), (36,255,12), 2)
            st.image(opencv_image, channels="BGR")
            break

df = pd.DataFrame({'a':[1,2,3,4],'b':[11,22,33,44], 'c':[111,222,333,444]})

for a, b, c in df.itertuples(index=False):
    st.write( a, b, c)

# if uploaded_file is not None:
#     # Convert the file to an opencv image.
#     file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
#     opencv_image = cv2.imdecode(file_bytes, 1)

#     # Now do something with the image! For example, let's display it:
#     st.image(opencv_image, channels="BGR")