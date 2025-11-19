from keras.models import load_model
from keras.preprocessing import image
import cv2
import numpy as np
import eel
import threading

eel.init(r"D:\stress detection\web")

face_classifier = cv2.CascadeClassifier(r"D:\stress detection\haarcascade_frontalface_default.xml")
classifier = load_model(r"D:\stress detection\model.h5")

emotion_labels = ['Angry','Disgust','Fear','Happy','Neutral', 'Sad', 'Surprise']

cap = cv2.VideoCapture(0)

running = False

def detect_stress():
    global running, cap

    while running:
        ret, frame = cap.read()
        if not ret:
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,255), 2)

            roi_gray = gray[y:y+h, x:x+w]
            roi_gray = cv2.resize(roi_gray, (48,48), interpolation=cv2.INTER_AREA)

            roi = roi_gray.astype("float") / 255.0
            roi = np.expand_dims(roi, axis=0)
            roi = np.expand_dims(roi, axis=3)

            prediction = classifier.predict(roi)[0]
            label = emotion_labels[np.argmax(prediction)]

            if label in ['Fear','Angry','Sad']:
                label = 'highly stressed'
            elif label in ['Disgust','Neutral']:
                label = 'low stressed'
            else:
                label = 'not stressed'

            cv2.putText(frame, label, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)

        cv2.imshow("Emotion Detector", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            running = False

    cap.release()
    cv2.destroyAllWindows()



@eel.expose
def start():
    """Start detection thread"""
    global running
    if not running:
        running = True
        threading.Thread(target=detect_stress, daemon=True).start()


@eel.expose
def stop():
    """Stop detection"""
    global running
    running = False


eel.start("index.html", port=8080)
