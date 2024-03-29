from flask import Flask,jsonify,request,render_template
from utils.speechToText import get_large_audio_transcription
from utils.base64Tomp3 import base64Tomp3
from flask_socketio import SocketIO
import os

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/speechToText',methods=['GET','POST'])
def decoding_mp3():
    if request.method == 'POST':
        encoded_string = request.json['base64']
        mp3_file = open(os.getcwd()+'/files/temp.mp3','wb')
        decode_string = base64Tomp3(encoded_string)
        mp3_file.write(decode_string)
        path = 'files/temp.mp3'
        full_text = get_large_audio_transcription(path,socketio)
        return jsonify({"text":full_text})
    return render_template('index.html')



if __name__=='__main__':
    socketio.run(app,host='localhost',port=5001,debug=True)
