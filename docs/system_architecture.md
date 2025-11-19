System Architecture:

 ┌────────────────────┐
 │      Webcam        │
 └─────────┬──────────┘
           │ Frame
           ▼
 ┌────────────────────┐
 │   Face Detector    │ (Haar cascade)
 └─────────┬──────────┘
           │ Cropped Face
           ▼
 ┌────────────────────┐
 │ Emotion Classifier │ (CNN Model)
 └─────────┬──────────┘
           │ Emotion Label
           ▼
 ┌─────────────────────────────┐
 │ Stress Level Classification │
 └─────────┬───────────────────┘
           │ Stress Result
           ▼
 ┌────────────────────┐
 │    UI Rendering    │
 └────────────────────┘
