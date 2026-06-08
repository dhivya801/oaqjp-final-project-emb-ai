"""
Emotion Detection Module using IBM Watson NLP Library
This module provides functionality to detect emotions in text using the Watson NLP library.
"""

import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


def emotion_detector(text_to_analyze):
    """
    Analyze the emotion of the provided text using IBM Watson NLP.
    
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
    
    # Set up the authenticator (URL and API key would be set from environment)
    authenticator = IAMAuthenticator(apikey='your-api-key-here')
    nlu = NaturalLanguageUnderstandingV1(
        version='2021-08-01',
        authenticator=authenticator,
        service_url='your-service-url-here'
    )
    
    try:
        # Analyze the text for emotions
        response = nlu.analyze(
            text=text_to_analyze,
            features=Features(emotion=EmotionOptions())
        )
        
        # Extract emotion scores from the response
        emotion_scores = response.result['emotion']['document']['emotion']
        
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
    
    except Exception as e:
        # Handle errors
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            'status_code': 400
        }
