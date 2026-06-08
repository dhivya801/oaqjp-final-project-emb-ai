# Emotion Detector

An emotion detection application using IBM Watson NLP Library that analyzes text and detects emotions including anger, disgust, fear, joy, and sadness.

## Features

- **Emotion Detection**: Analyzes text to detect five emotions: anger, disgust, fear, joy, and sadness
- **REST API**: Flask web server for easy integration with other applications
- **Error Handling**: Comprehensive error handling for invalid inputs
- **Unit Tests**: Complete test suite to validate functionality
- **Static Code Analysis**: Pylint integration for code quality

## Project Structure

```
emotion/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── test_emotion_detection.py
├── server.py
└── README.md
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd emotion
```

2. Install required dependencies:
```bash
pip install ibm-watson ibm-cloud-sdk-core flask pylint
```

## Usage

### As a Python Module

```python
from EmotionDetection.emotion_detection import emotion_detector

result = emotion_detector("I am so happy!")
print(result)
```

### As a Flask Web Service

1. Start the server:
```bash
python server.py
```

2. Make a POST request:
```bash
curl -X POST http://localhost:5000/emotion_detector \
  -H "Content-Type: application/json" \
  -d '{"text": "I am feeling great today"}'
```

## API Endpoints

### POST /emotion_detector
Analyzes emotion in the provided text.

**Request:**
```json
{
  "text": "Your text here"
}
```

**Response (Success - 200):**
```json
{
  "anger": 0.1,
  "disgust": 0.0,
  "fear": 0.0,
  "joy": 0.9,
  "sadness": 0.0,
  "dominant_emotion": "joy"
}
```

**Response (Error - 400):**
```json
{
  "error": "Please provide non-empty text"
}
```

### GET /health
Health check endpoint to verify server is running.

## Testing

Run the unit tests:
```bash
python -m pytest test_emotion_detection.py
# or
python -m unittest test_emotion_detection.py
```

## Code Quality

Run static code analysis:
```bash
pylint server.py
pylint EmotionDetection/emotion_detection.py
```

## Watson NLP Integration

This application uses the IBM Watson Natural Language Understanding API to detect emotions in text. The API returns emotion scores for:

- **Anger**: Likelihood of anger
- **Disgust**: Likelihood of disgust
- **Fear**: Likelihood of fear
- **Joy**: Likelihood of joy
- **Sadness**: Likelihood of sadness

## Error Handling

The application handles:
- Blank or empty input (returns 400 status code)
- Missing API credentials (handled gracefully)
- Invalid API requests (returns appropriate error messages)

## Author

Emotion Detection Application

## License

This project is open source and available under the MIT License.
