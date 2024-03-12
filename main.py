from flask import Flask, jsonify, request, send_file
from util.tts import CharacterTTS

MODEL_PATH = "assets/weights/Szrv3.pth"
AUDIO_PATH = "assets/audio/output.wav"

app = Flask(__name__)
tts = CharacterTTS(MODEL_PATH)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/tts', methods=['POST'])
def post_tts_request():
    data = request.json
    text = data.get('text')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    tts.text_to_speech_kr(text, AUDIO_PATH)

    return send_file(AUDIO_PATH)


if __name__ == '__main__':
    app.run()
