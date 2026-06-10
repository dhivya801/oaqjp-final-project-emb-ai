# Final Project

## Emotion Detection Application using IBM Watson NLP Library

This is the **Final Project** for the IBM AI Engineering Professional Certificate course. The application uses the Watson NLP library to detect emotions in text, including anger, disgust, fear, joy, and sadness.

## Features

- **Emotion Detection**: Analyzes text to detect five emotions using Watson NLP
- **REST API**: Flask web server with `/emotionDetector` endpoint
- **Error Handling**: Returns appropriate messages for blank input (status 400)
- **Unit Tests**: Complete test suite validating all five emotions
- **Static Code Analysis**: Pylint score of 10.00/10

## Project Structure

```
oaqjp-final-project-emb-ai/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── templates/
│   └── index.html
├── server.py
├── test_emotion_detection.py
└── README.md
```

## Installation

```bash
pip install requests flask pylint
```

## Usage

### Start the Flask Server
```bash
python server.py
```

### Access the Application
Open `http://localhost:5000` in your browser.

## API Endpoint

### GET /emotionDetector
Analyzes emotion in the provided text.

**Request:**
```
GET /emotionDetector?textToAnalyze=I+love+this+product
```

**Response:**
```
For the given statement, the system response is 'anger': 0.006, 'disgust': 0.002, 'fear': 0.009, 'joy': 0.971 and 'sadness': 0.011. The dominant emotion is joy.
```

## Testing

```bash
python -m unittest test_emotion_detection.py
```

## Code Quality

```bash
pylint server.py
```

## Author

Final Project - Emotion Detection Application
