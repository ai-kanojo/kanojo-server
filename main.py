import os

from flask import Flask, jsonify, request
from util.tts import text_to_speech

app = Flask(__name__)

# mp4 파일이 업로드되는 경로 설정
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    # 사용자가 파일을 선택하지 않고 form을 제출했을 경우
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # 파일이 있는 경우
    if file:
        # 안전한 파일 이름을 생성 (secure_filename 사용 권장)
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        return jsonify({'message': f'File {filename} uploaded successfully'}), 200


if __name__ == '__main__':
    app.run()
