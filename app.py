from flask import Flask, render_template, request, jsonify
import json
from emotion_model import predict_emotion

app = Flask(__name__)

# गाँव का data load करना (JSON file से)
with open('gaav_data.json', 'r', encoding='utf-8') as f:
    gaav_data = json.load(f)

@app.route('/')
def home():
    return render_template('index.html', data=gaav_data)

@app.route('/analyze_emotion', methods=['POST'])
def analyze_emotion():
    text = request.json.get('text')
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    emotion = predict_emotion(text)
    return jsonify({'emotion': emotion})

if __name__ == '__main__':
    app.run(debug=True)
