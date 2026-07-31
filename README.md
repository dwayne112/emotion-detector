# Emotion Detector

Final Project for IBM's "Developing AI Applications with Python and Flask" course.

## Description

A Python web application using Flask that integrates IBM Watson NLP to detect emotions in text. The application analyzes text input and returns scores for anger, disgust, fear, joy, and sadness, along with the dominant emotion.

## Project Structure

```
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── templates/
│   └── index.html
├── static/
│   └── mywebscript.js
├── tests/
│   └── test_emotion_detection.py
├── server.py
└── requirements.txt
```

## Usage

```python
from EmotionDetection.emotion_detection import emotion_detector
emotion_detector("I am so happy today!")
# Returns: {'anger': 0.006, 'disgust': 0.001, 'fear': 0.003, 'joy': 0.954, 'sadness': 0.036, 'dominant_emotion': 'joy'}
```

Run the Flask server:
```bash
python server.py
```
Then visit http://localhost:5000

## Technologies

- Python
- Flask
- IBM Watson NLP Emotion Prediction API
- unittest