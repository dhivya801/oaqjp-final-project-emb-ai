const textInput = document.getElementById('textInput');
const submitButton = document.getElementById('submitButton');
const errorMessage = document.getElementById('errorMessage');
const dominantEmotion = document.getElementById('dominantEmotion');
const emotionScores = document.getElementById('emotionScores');
const scoreBars = document.getElementById('scoreBars');

function setFeedback(message) {
    errorMessage.textContent = message;
    errorMessage.classList.add('show');
}

function clearFeedback() {
    errorMessage.classList.remove('show');
    errorMessage.textContent = '';
}

function renderScores(data) {
    dominantEmotion.textContent = data.dominant_emotion ? data.dominant_emotion.toUpperCase() : 'UNKNOWN';
    document.getElementById('angerScore').textContent = `${(data.anger * 100).toFixed(1)}%`;
    document.getElementById('disgustScore').textContent = `${(data.disgust * 100).toFixed(1)}%`;
    document.getElementById('fearScore').textContent = `${(data.fear * 100).toFixed(1)}%`;
    document.getElementById('joyScore').textContent = `${(data.joy * 100).toFixed(1)}%`;
    document.getElementById('sadnessScore').textContent = `${(data.sadness * 100).toFixed(1)}%`;

    scoreBars.innerHTML = '';
    const emotions = [
        { label: 'Anger', value: data.anger },
        { label: 'Disgust', value: data.disgust },
        { label: 'Fear', value: data.fear },
        { label: 'Joy', value: data.joy },
        { label: 'Sadness', value: data.sadness }
    ];

    emotions.forEach(emotion => {
        const row = document.createElement('div');
        row.className = 'bar-row';

        const label = document.createElement('span');
        label.textContent = emotion.label;

        const barWrapper = document.createElement('div');
        barWrapper.className = 'bar';

        const barFill = document.createElement('div');
        barFill.className = 'bar-fill';
        barFill.style.width = `${Math.min(Math.max(emotion.value * 100, 2), 100)}%`;

        barWrapper.appendChild(barFill);
        row.appendChild(label);
        row.appendChild(barWrapper);
        scoreBars.appendChild(row);
    });
}

async function analyzeEmotion() {
    const text = textInput.value.trim();
    clearFeedback();

    if (!text) {
        setFeedback('Please enter some text before analyzing.');
        return;
    }

    submitButton.disabled = true;
    submitButton.textContent = 'Analyzing...';

    try {
        const response = await fetch('/emotion_detector', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || 'Unable to analyze the text.');
        }

        renderScores(data);
    } catch (error) {
        setFeedback(error.message);
    } finally {
        submitButton.disabled = false;
        submitButton.textContent = 'Analyze Emotion';
    }
}

submitButton.addEventListener('click', analyzeEmotion);
textInput.addEventListener('keydown', event => {
    if (event.key === 'Enter' && event.ctrlKey) {
        analyzeEmotion();
    }
});
