import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from EmotionDetection.emotion_detection import emotion_detector, format_result

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector_joy(self):
        result = emotion_detector("I love this")
        self.assertIsNotNone(result.get('joy'))
        self.assertEqual(result.get('dominant_emotion'), 'joy')
    
    def test_emotion_detector_anger(self):
        result = emotion_detector("I am so frustrated and angry")
        self.assertIsNotNone(result.get('anger'))
        self.assertEqual(result.get('dominant_emotion'), 'anger')
    
    def test_emotion_detector_sadness(self):
        result = emotion_detector("I am so sad today")
        self.assertIsNotNone(result.get('sadness'))
    
    def test_emotion_detector_fear(self):
        result = emotion_detector("I am very scared")
        self.assertIsNotNone(result.get('fear'))
    
    def test_emotion_detector_disgust(self):
        result = emotion_detector("This is disgusting")
        self.assertIsNotNone(result.get('disgust'))
    
    def test_emotion_detector_none(self):
        result = emotion_detector("")
        self.assertEqual(result.get('status_code'), 400)
        self.assertIsNone(result.get('dominant_emotion'))
    
    def test_format_result(self):
        test_dict = {'joy': 0.95, 'sadness': 0.03, 'anger': 0.01, 'fear': 0.005, 'disgust': 0.003, 'surprise': 0.002, 'dominant_emotion': 'joy'}
        formatted = format_result(test_dict)
        self.assertIn("'joy': 0.95", formatted)
        self.assertIn("'dominant_emotion': 'joy'", formatted)

if __name__ == '__main__':
    unittest.main()
