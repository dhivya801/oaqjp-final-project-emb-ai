"""
Unit tests for the Emotion Detection module
"""

import unittest
from EmotionDetection.emotion_detection import emotion_detector
class TestEmotionDetector(unittest.TestCase):
    """Test cases for the emotion_detector function"""
    def test_emotion_detector_joy(self):
        """Test emotion detection for joyful text"""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')
        self.assertEqual(result['status_code'], 200)
    def test_emotion_detector_anger(self):
        """Test emotion detection for angry text"""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')
        self.assertEqual(result['status_code'], 200)
    def test_emotion_detector_disgust(self):
        """Test emotion detection for disgusted text"""
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')
        self.assertEqual(result['status_code'], 200)
    def test_emotion_detector_sadness(self):
        """Test emotion detection for sad text"""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')
        self.assertEqual(result['status_code'], 200)
    def test_emotion_detector_fear(self):
        """Test emotion detection for fearful text"""
        result = emotion_detector("I am really afraid of this")
        self.assertEqual(result['dominant_emotion'], 'fear')
        self.assertEqual(result['status_code'], 200)
    def test_emotion_detector_blank_input(self):
        """Test emotion detection with blank input"""
        result = emotion_detector("")
        self.assertIsNone(result['dominant_emotion'])
        self.assertEqual(result['status_code'], 400)
    def test_emotion_detector_none_input(self):
        """Test emotion detection with None input"""
        result = emotion_detector(None)
        self.assertIsNone(result['dominant_emotion'])
        self.assertEqual(result['status_code'], 400)


if __name__ == '__main__':
    unittest.main()
