import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
from flask_socketio import emit



r = sr.Recognizer()


def get_large_audio_transcription(path,socketio):
    sound = AudioSegment.from_file(path)
    chunks = split_on_silence(sound,
        min_silence_len = 500,
        silence_thresh = sound.dBFS-14,
        keep_silence=500,
    )
    folder_name = "audio-chunks"
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    for i, audio_chunk in enumerate(chunks, start=1):
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            try:
                text = r.recognize_google(audio_listened)
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                socketio.emit('speech',text)
                socketio.sleep(0.5)
                print(chunk_filename, ":", text)
                whole_text += text
    return whole_text

