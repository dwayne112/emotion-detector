# Emotion Detector

An AI-powered Emotion Detection web application built with Python, Flask, and IBM Watson NLP library.

## Project Overview

This project implements an emotion detection tool using IBM Watson Natural Language Processing (NLP) library. The application analyzes text input and identifies the emotion expressed (joy, sadness, anger, fear, disgust, surprise).

## Features

- Emotion detection using IBM Watson NLP
- REST API built with Flask
- Unit testing with pytest
- Error handling for invalid inputs
- Static code analysis with pylint

## Installation

```bash
pip install ibm-watson-machine-learning flask pytest pylint
```

## Usage

```python
from EmotionDetection.emotion_detection import emotion_detector

result = emotion_detector("I am so happy today!")
print(result)
```

## Project Structure

- `EmotionDetection/` - Main package
  - `__init__.py` - Package initialization
  - `emotion_detection.py` - Emotion detection module
- `tests/` - Test suite
  - `test_emotion_detection.py` - Unit tests
- `server.py` - Flask web application

## Author

Dwayne Taylor

## License

MIT
