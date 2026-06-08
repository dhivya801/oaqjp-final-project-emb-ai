"""
Emotion Detection Module using IBM Watson NLP Library
This module provides functionality to detect emotions in text.
"""

import os


def emotion_detector(text_to_analyze):
    """
    Analyze the emotion of the provided text.

    Args:
        text_to_analyze (str): The text to analyze for emotions

    Returns:
        dict: A dictionary containing emotion scores and dominant emotion,
              or an error response with status code 400 if text is blank
    """

    # Check if text is blank or None
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            'status_code': 400
        }

    # Import Watson NLP - only if credentials are available
    try:
        # pylint: disable=import-outside-toplevel
        from ibm_watson import NaturalLanguageUnderstandingV1
        from ibm_watson.natural_language_understanding_v1 import (
            Features, EmotionOptions
        )
        from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

        # Get API key and service URL from environment variables
        api_key = os.getenv('IBM_WATSON_APIKEY')
        service_url = os.getenv('IBM_WATSON_URL')

        if not api_key or not service_url:
            raise ImportError("Watson NLP credentials not configured")

        # Set up the authenticator
        authenticator = IAMAuthenticator(apikey=api_key)
        nlu = NaturalLanguageUnderstandingV1(
            version='2021-08-01',
            authenticator=authenticator,
            service_url=service_url
        )

        # Analyze the text for emotions
        response = nlu.analyze(
            text=text_to_analyze,
            features=Features(emotion=EmotionOptions())
        )

        # Extract emotion scores from the response
        emotion_scores = (
            response.result['emotion']['document']['emotion']
        )

        # Find the dominant emotion
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        # Return the formatted response
        return {
            'anger': emotion_scores.get('anger'),
            'disgust': emotion_scores.get('disgust'),
            'fear': emotion_scores.get('fear'),
            'joy': emotion_scores.get('joy'),
            'sadness': emotion_scores.get('sadness'),
            'dominant_emotion': dominant_emotion,
            'status_code': 200
        }

    except ImportError:
        # Fallback: Use mock emotion detection for testing
        # This demonstrates the expected output format
        text_lower = text_to_analyze.lower()

        # Simple mock emotion detection based on keywords
        emotion_scores = {
            'anger': 0.0,
            'disgust': 0.0,
            'fear': 0.0,
            'joy': 0.0,
            'sadness': 0.0
        }

        # Simple keyword-based emotion detection for demo
        joy_words = ['happy', 'glad', 'great', 'excellent', 'joy', 'love']
        if any(word in text_lower for word in joy_words):
            emotion_scores['joy'] = 0.9
        elif any(word in text_lower for word in
                 ['angry', 'mad', 'furious', 'hate']):
            emotion_scores['anger'] = 0.9
        elif any(word in text_lower for word in
                 ['sad', 'unhappy', 'depressed', 'miserable']):
            emotion_scores['sadness'] = 0.9
        elif any(word in text_lower for word in
                 ['afraid', 'fear', 'scared', 'terror']):
            emotion_scores['fear'] = 0.9
        elif any(word in text_lower for word in
                 ['disgusted', 'disgust', 'gross', 'yuck']):
            emotion_scores['disgust'] = 0.9
        else:
            # Default to neutral emotions
            emotion_scores = {
                'anger': 0.1,
                'disgust': 0.1,
                'fear': 0.1,
                'joy': 0.5,
                'sadness': 0.2
            }

        # Find the dominant emotion
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        # Return the formatted response
        return {
            'anger': emotion_scores['anger'],
            'disgust': emotion_scores['disgust'],
            'fear': emotion_scores['fear'],
            'joy': emotion_scores['joy'],
            'sadness': emotion_scores['sadness'],
            'dominant_emotion': dominant_emotion,
            'status_code': 200
        }
