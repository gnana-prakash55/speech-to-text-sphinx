from flask import Flask,jsonify
from utils.speechToText import get_large_audio_transcription
from utils.base64Tomp3 import base64Tomp3
import os

app = Flask(__name__)


@app.route('/speechToText')
def decoding_mp3():
    mp3_file = open(os.getcwd()+'/files/temp.mp3','wb')
    decode_string = base64Tomp3(url='http://localhost:8000/')
    mp3_file.write(decode_string)
    path = 'files/temp.mp3'
    full_text = get_large_audio_transcription(path)
    return jsonify({"text":full_text})


if __name__=='__main__':
    app.run(host='localhost',port=5001,debug=True)