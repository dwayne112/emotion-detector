"""
Unit Tests for Emotion Detection Module
"""
import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from EmotionDetection.emotion_detection import emotion_detector, format_result


def test_emotion_detector_joy():
    """Test emotion detector with happy text"""
    result = emotion_detector("I am so happy today!")
    assert 'joy' in result
    assert 'sadness' in result
    assert 'anger' in result
    assert 'fear' in result
    assert 'disgust' in result
    assert 'surprise' in result
    assert result['joy'] > result['sadness']


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


def test_format_result():
    """Test format_result helper function"""
    result = emotion_detector("I am so happy today!")
    formatted = format_result(result)
    assert 'joy' in formatted
    assert '0.854' in formatted
