from flask import Flask, jsonify, request, send_file
from util.tts import CharacterTTS
from util.gptapi import GPTApi
from util.stt import speech_to_text
import os

MODEL_PATH = "assets/weights/Szrv3.pth"
AUDIO_PATH = "assets/audio/output.wav"

ASSISTANT_KR_ID='asst_TnuTyENYP7YIFjXDaVYuvEg5'
ASSISTANT_JP_ID='asst_o9Cpot5JslElwcPaDr7JMrQS'

app = Flask(__name__)
tts = CharacterTTS(MODEL_PATH)
gpt = GPTApi(ASSISTANT_KR_ID)
gpt_language = 'kr'

# mp4 파일이 업로드되는 경로 설정
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def hello_world():
    return 'Hello World!'



@app.route('/tts', methods=['POST'])
def post_tts_request():
    """
    텍스트 보내면 스즈란목소리로 바꿔서 반환함
    """
    data = request.json
    text = data.get('text')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    tts.text_to_speech_kr(text, AUDIO_PATH)

    return send_file(AUDIO_PATH)


@app.route('/upload', methods=['POST'])
def upload_file():
    """
    미구현
    파일올리면 파일이름과 텍스트를 알려줌
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    # 사용자가 파일을 선택하지 않고 form을 제출했을 경우
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # 파일이 있는 경우
    if file:
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        text = speech_to_text(file_path)
        return jsonify({'message': f'File {filename} uploaded successfully',
                        'text': text}), 200


@app.route('/askai', methods=['POST'])
def ask_ai():
    """
    텍스트로 물어보면 텍스트로 답해줌
    """
    global gpt_language
    global gpt
    if gpt_language != 'kr':
        gpt_language = 'kr'
        gpt = GPTApi(ASSISTANT_KR_ID)

    data = request.json
    text = data.get('text')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    result = gpt.send(text)
    print(result)

    return jsonify({'result': result})

@app.route('/pipeline', methods=['POST'])
def pipeline():
    """
    음성파일을 받아서 과정을 다 해주는 파이프라인
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    
    # 사용자가 파일을 선택하지 않고 form을 제출했을 경우
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # 파일이 있는 경우
    if file:
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        text = speech_to_text(file_path)
        answer = gpt.send(text)
        tts.text_to_speech_kr(answer, AUDIO_PATH)

        return send_file(AUDIO_PATH)

@app.route('/ttsjp', methods=['POST'])
def post_tts_jp_request():
    """
    텍스트 보내면 스즈란목소리로 바꿔서 반환함
    """
    data = request.json
    text = data.get('text')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    tts.text_to_speech_jp(text, AUDIO_PATH)

    return send_file(AUDIO_PATH)

@app.route('/askaijp', methods=['POST'])
def ask_ai_jp():
    """
    텍스트로 물어보면 텍스트로 답해줌
    """
    global gpt_language
    global gpt
    if gpt_language != 'jp':
        gpt_language = 'jp'
        gpt = GPTApi(ASSISTANT_JP_ID)

    data = request.json
    text = data.get('text')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    result = gpt.send(text)
    print(result)

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
