"""
Flask server for Emotion Detection application.
This module deploys the emotion detector as a web application using Flask.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_detect():
    """
    Route to analyze emotion in provided text.
    Receives text via query parameter textToAnalyze.
    Returns a formatted string response with emotion scores.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    return (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is <b>{response['dominant_emotion']}</b>."
    )


@app.route("/")
def render_index_page():
    """
    Route to render the index page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
