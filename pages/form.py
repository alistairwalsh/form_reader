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

def draw_bounding(opencv_image, data_df):
    '''Takes an image and a dataframe with coordinates and text and outputs the modified image'''
    for x, y, w, h, t in data_df[['left','top','width','height','text']].itertuples(index = False):
        st.write(x,y,w,h,t)
        cv2.rectangle(opencv_image, (x,y), (x + w, y + h), (36,255,12), 2)
        cv2.putText(opencv_image, str(t), (x, y-6), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 1)
    return opencv_image

if uploaded_file is not None:
        images = convert_from_bytes(uploaded_file.read())
        for page in images:
            opencv_image = np.array(page)
            st.image(page, use_column_width=True)
            
            data_df = pytesseract.image_to_data(page, output_type=Output.DATAFRAME)
            st.dataframe(data_df)

            img = draw_bounding(opencv_image, data_df)
            #rehab = data_df.loc[26,['left','top','width','height','text']]
            #(x, y), (x + w, y + h)
            #st.write(rehab)
            #cv2.rectangle(opencv_image, (rehab['left'], rehab['top']), (rehab['left'] + rehab['width'], rehab['top'] + rehab['height']), (36,255,12), 2)
            st.image(img, channels="BGR")
            break

#df = pd.DataFrame({'a':[1,2,3,4],'b':[11,22,33,44], 'c':[111,222,333,444]})

#for a, b, c in df.itertuples(index=False):
#    st.write( a, b, c)

# if uploaded_file is not None:
#     # Convert the file to an opencv image.
#     file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
#     opencv_image = cv2.imdecode(file_bytes, 1)

#     # Now do something with the image! For example, let's display it:
#     st.image(opencv_image, channels="BGR")

# x,y,w,h = cv2.boundingRect(contour)
# image = cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 1)
# cv2.putText(image, 'Fedex', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

