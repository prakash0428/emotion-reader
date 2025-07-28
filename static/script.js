async function analyzeEmotion() {
    const text = document.getElementById('userText').value.trim();

    if (!text) {
        alert("Kripya pehle kuch text likhiye!");
        return;
    }

    const response = await fetch('/analyze_emotion', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: text })
    });

    const data = await response.json();

    if (data.emotion) {
        document.getElementById('result').innerText = Emotion: ${data.emotion};
    } else {
        document.getElementById('result').innerText = 'Kuch galti ho gayi 😔';
    }
}
