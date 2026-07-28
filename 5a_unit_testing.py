import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from EmotionDetection.emotion_detection import emotion_detector, format_result


class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector_joy(self):
        result = emotion_detector("I am so happy today!")
        self.assertIn('joy', result)
        self.assertIn('sadness', result)
        self.assertIn('anger', result)
        self.assertIn('fear', result)
        self.assertIn('disgust', result)
        self.assertIn('surprise', result)
        self.assertIn('dominant_emotion', result)
        self.assertEqual(result['status_code'], 200)

    def test_emotion_detector_sadness(self):
        result = emotion_detector("I feel very sad and upset")
        self.assertIn('joy', result)
        self.assertIn('sadness', result)
        self.assertIn('dominant_emotion', result)
        self.assertEqual(result['status_code'], 200)

    def test_emotion_detector_anger(self):
        result = emotion_detector("I am so frustrated and angry")
        self.assertIn('anger', result)
        self.assertIn('dominant_emotion', result)
        self.assertEqual(result['status_code'], 200)

    def test_emotion_detector_disgust(self):
        result = emotion_detector("This is disgusting")
        self.assertIn('disgust', result)
        self.assertIn('dominant_emotion', result)
        self.assertEqual(result['status_code'], 200)

    def test_emotion_detector_fear(self):
        result = emotion_detector("I am very scared")
        self.assertIn('fear', result)
        self.assertIn('dominant_emotion', result)
        self.assertEqual(result['status_code'], 200)

    def test_emotion_detector_blank(self):
        result = emotion_detector("")
        self.assertEqual(result['status_code'], 400)
        self.assertIsNone(result['joy'])
        self.assertIsNone(result['anger'])

    def test_emotion_detector_none(self):
        result = emotion_detector(None)
        self.assertEqual(result['status_code'], 400)
        self.assertIsNone(result['joy'])

    def test_format_result(self):
        result = {'joy': 0.85, 'sadness': 0.03, 'anger': 0.02, 'fear': 0.01, 'disgust': 0.01, 'surprise': 0.0, 'dominant_emotion': 'joy'}
        formatted = format_result(result)
        self.assertIn('joy', formatted)
        self.assertIn('dominant_emotion', formatted)


if __name__ == '__main__':
    unittest.main()
