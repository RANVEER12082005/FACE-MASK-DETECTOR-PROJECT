import ssl
import certifi
ssl._create_default_https_context = ssl.create_default_context

import numpy as np
import cv2
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

def load_mask_model(model_path="models/mask_detector.h5"):
    model = load_model(model_path)
    return model

def predict_mask(face_img, model):
    face = cv2.resize(face_img, (224, 224))
    face = img_to_array(face)
    face = preprocess_input(face)
    face = np.expand_dims(face, axis=0)

    (mask, withoutMask) = model.predict(face, verbose=0)[0]

    label      = "Mask" if mask > withoutMask else "No Mask"
    confidence = max(mask, withoutMask) * 100
    color      = (0, 255, 0) if label == "Mask" else (0, 0, 255)

    return label, confidence, color