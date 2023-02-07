from flask import Flask, request, send_file
import os

app = Flask(__name__)


def model_request(text):
    # TODO 모델 가져와서 텍스트를 input으로 output으로 파일이름
    return "notifications-sound-127856.mp3"


@app.route("/api/predict/", methods=['POST'])
def predict_sound():
    text = request.json['sentence']

    file_name = model_request(text)
    path = "./temp/"
    url = os.path.join(path, file_name)
    return send_file(url, "multipart/form-data", as_attachment=True)


@app.route('/')
def hello_world():
    return "Hello World"


if __name__ == '__main__':
    app.run()
