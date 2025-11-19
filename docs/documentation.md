<details>
<summary><strong>Overview</strong></summary>

The Stress Detection System is a real-time emotion and stress-level classification application built using OpenCV, Keras, and a lightweight Eel web interface.  
It captures webcam frames, detects faces, predicts emotional states using a trained CNN model, and maps those emotions into stress categories such as **highly stressed**, **low stressed**, or **not stressed**.

The system is fully modular, making it easy to extend, retrain, or integrate into other applications.

</details>


<details>
<summary><strong>Key Components</strong></summary>

**Face Detection:**  
Uses Haar Cascade classifier to locate faces in each frame.

**Emotion Classification:**  
A pre-trained Keras CNN model predicts one of seven emotions:  
*Angry, Disgust, Fear, Happy, Neutral, Sad, Surprise.*

**Stress Mapping Logic:**  
A configurable mapping converts emotion → stress level.

**Real-Time Processing:**  
Continuously reads frames from the webcam and overlays results.

**Eel UI:**  
Provides a simple webpage with controls to start/stop detection.

</details>


<details>
<summary><strong>Workflow Summary</strong></summary>

1. Webcam captures a frame  
2. Convert to grayscale  
3. Detect faces  
4. Extract + preprocess face regions  
5. Predict emotion using CNN model  
6. Map emotion → stress level  
7. Display stress label on the video feed  
8. Repeat in real time until stopped  

</details>
