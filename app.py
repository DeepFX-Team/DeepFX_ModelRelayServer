from flask import Flask, request, send_file

app = Flask(__name__)


@app.route("/api/predict/", methods=['POST'])
def predict_sound():
    text = request.json

    path = "./temp/"
    return send_file(path + "notifications-sound-127856.mp3",
                     "multipart/form-data", as_attachment=True)


@app.route('/')
def hello_world():
    return "Hello World"


if __name__ == '__main__':
    app.run()
