import os
import cv2
import numpy as np
from stress_detection.detector import detect
from stress_detection.model_loader import load_models

def test_load_models():
    face, model = load_models()
    assert face is not None
    assert model is not None

def test_detect_no_camera_image():
    # create a blank image
    img = np.zeros((480,640,3), dtype=np.uint8)
    face, model = load_models()
    results = detect(img, face, model)
    assert isinstance(results, list)
