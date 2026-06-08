"""
Flask server for Emotion Detection application
Provides REST API endpoints for emotion detection
"""

from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/emotion_detector', methods=['POST'])
def analyze_emotion():
    """
    POST endpoint to analyze emotion in provided text
    Request body should contain: {"text": "your text here"}
    Returns: JSON response with emotion scores and dominant emotion
    """
    
    try:
        # Get the text from the request body
        data = request.get_json()
        
        # Check if text is provided
        if not data or 'text' not in data:
            return jsonify({'error': 'No text provided'}), 400
        
        text_to_analyze = data.get('text', '')
        
        # Call the emotion detector function
        result = emotion_detector(text_to_analyze)
        
        # Handle blank input error
        if result['status_code'] == 400:
            return jsonify({'error': 'Please provide non-empty text'}), 400
        
        # Return the formatted response
        return jsonify({
            'anger': result['anger'],
            'disgust': result['disgust'],
            'fear': result['fear'],
            'joy': result['joy'],
            'sadness': result['sadness'],
            'dominant_emotion': result['dominant_emotion']
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
