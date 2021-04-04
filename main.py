from flask import Flask,jsonify,request
from utils.speechToText import get_large_audio_transcription
from utils.base64Tomp3 import base64Tomp3
import os

app = Flask(__name__)


@app.route('/speechToText',methods=['POST'])
def decoding_mp3():
    if request.method == 'POST':
        encoded_string = request.json['base64']
        mp3_file = open(os.getcwd()+'/files/temp.mp3','wb')
        decode_string = base64Tomp3(encoded_string)
        mp3_file.write(decode_string)
        path = 'files/temp.mp3'
        full_text = get_large_audio_transcription(path)
        return jsonify({"text":full_text})
    return jsonify({"error":"Something went wrong"})

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5001,debug=False)
