import torch
import cv2
from pathlib import Path
import pytesseract


model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp18/weights/best.pt')

img_path = 'datasets/test/images/nom_image_377_jpg.rf.758137bdcf1eddb782020f3ba59a1e10.jpg'
img = cv2.imread(img_path)
results = model(img)

results.show()


# Extraire les boîtes de détection
detections = results.xyxy[0]  # coordonnées des boîtes

for *box, conf, cls in detections:
    x1, y1, x2, y2 = map(int, box)
    cropped_img = img[y1:y2, x1:x2]
    text = pytesseract.image_to_string(cropped_img)
    print(f'Texte détecté : {text}')