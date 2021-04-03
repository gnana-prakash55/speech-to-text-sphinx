from flask import Flask,jsonify
from utils.speechToText import get_large_audio_transcription

app = Flask(__name__)


@app.route('/speechToText')
def hello():
    path = 'files/Welcome.mp3'
    full_text = get_large_audio_transcription(path)
    return jsonify({"text":full_text})


if __name__=='__main__':
    app.run(host='localhost',port=5001,debug=True)