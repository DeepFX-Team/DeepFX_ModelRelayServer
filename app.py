import base64
import wave

from flask import Flask, request
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


def model_request(json_params):
    response = requests.post(url="http://127.0.0.1:3013/run_inference", json=json_params)
    return response.json().get("audio")


def service_request(file_url, jwt):
    target = open(file_url, "rb")
    response = requests.post(url="https://www.ljhhosting.com/api/sound/upload", files={"soundFile": target}, headers={'X-ACCESS-TOKEN': jwt})

    return response


@app.route("/api/predict/", methods=['POST'])
def predict_sound():
    json_params = request.json
    jwt = request.headers['X-ACCESS-TOKEN']

    file_name = (json_params.get("start")).get("prompt")
    file_bin = model_request(json_params)

    path = "./temp/"

    url = os.path.join(path, file_name + ".mp3")

    file_ptr = open(url, "wb")
    file_decode = base64.b64decode(file_bin)

    file_ptr.write(file_decode)
    file_ptr.close()

    response = service_request(url, jwt)

    return response.json()


@app.route('/')
def hello_world():
    return "Hello World"


if __name__ == '__main__':
    app.run()
