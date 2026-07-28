"""
Unit Tests for Emotion Detection Module
"""
import pytest
from EmotionDetection.emotion_detection import emotion_detector


def test_emotion_detector_joy():
    """Test emotion detector with happy text"""
    result = emotion_detector("I am so happy today!")
    assert 'joy' in result
    assert 'sadness' in result
    assert 'anger' in result
    assert 'fear' in result
    assert 'disgust' in result
    assert 'surprise' in result


def test_emotion_detector_sadness():
    """Test emotion detector with sad text"""
    result = emotion_detector("I feel very sad and upset")
    assert 'joy' in result
    assert 'sadness' in result


def test_emotion_detector_anger():
    """Test emotion detector with angry text"""
    result = emotion_detector("I am so frustrated and angry")
    assert 'anger' in result


def test_emotion_detector_blank():
    """Test emotion detector with blank input"""
    result = emotion_detector("")
    assert 'error' in result


def test_emotion_detector_none():
    """Test emotion detector with None input"""
    result = emotion_detector(None)
    assert 'error' in result
