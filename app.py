import streamlit as st
import torch
import cv2
import numpy as np
from PIL import Image
import pytesseract

#exp17 v0
#exp18 v1
#exp22 v2
model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp22/weights/best.pt')

def detect_text(image):
    results = model(image)
    detections = results.xyxy[0]
    return detections


class_colors = {
    0: (255, 0, 0),
    1: (0, 255, 0),
    2: (0, 0, 255),
    3: (255, 255, 0),
    4: (0, 255, 255)
}

class_name = {
    0: 'Titre',
    1: 'date',
    2: 'description',
    3: 'total',
    4: 'tva'
}


st.title("Détection de Texte sur Image avec YOLOv5")

uploaded_file = st.file_uploader("Choisissez une image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image = np.array(image)
    st.image(image, caption='Image Uploaded', use_column_width=True)
    
    with st.spinner('Detection en cours...'):
        detections = detect_text(image)
    
    st.subheader("Résultats de la Détection")
    for *box, conf, cls in detections:
        x1, y1, x2, y2 = map(int, box)
        cropped_img = image[y1:y2, x1:x2]

        color = class_colors.get(int(cls), (255, 255, 255))
        label = class_name.get(int(cls))

        text = pytesseract.image_to_string(cropped_img)
        st.write(f'{label} : {text}')
        
        cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
        cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
    
    st.image(image, caption='Image avec détection', use_column_width=True)
