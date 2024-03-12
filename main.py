from flask import Flask, jsonify, request
from util.tts import text_to_speech

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/tts', methods=['POST'])
def post_tts_request():
    data = request.json
    text = data.get('text')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    result = text_to_speech(text)

    return jsonify({'result': result})


if __name__ == '__main__':
    app.run()
