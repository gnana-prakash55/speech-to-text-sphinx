import base64
import os
import requests


def base64Tomp3(url):
    response = requests.get(url)
    encoded_string = response.json()['base64']
    decode_string = base64.b64decode(encoded_string.encode('utf-8'))
    print(type(decode_string))
    return decode_string

