"""
Executes the necessary tests
"""
import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """
    Class that executes the test_function
    """

    def test_emotion_detector_joy(self):
        """
        Test joy emotion
        """
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], "joy")

    def test_emotion_detector_anger(self):
        """
        Test anger emotion
        """
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], "anger")

    def test_emotion_detector_disgust(self):
        """
        Test disgust emotion
        """
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], "disgust")

    def test_emotion_detector_sadness(self):
        """
        Test sadness emotion
        """
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], "sadness")

    def test_emotion_detector_fear(self):
        """
        Test fear emotion
        """
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], "fear")

    def test_emotion_detector_blank(self):
        """
        Test blank input
        """
        result = emotion_detector("")
        self.assertIsNone(result['dominant_emotion'])

    def test_emotion_detector_none(self):
        """
        Test None input
        """
        result = emotion_detector(None)
        self.assertIsNone(result['dominant_emotion'])


unittest.main()