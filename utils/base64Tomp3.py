import base64
import os
import requests


def base64Tomp3(encoded_string):
    decode_string = base64.b64decode(encoded_string.encode('utf-8'))
    print(type(decode_string))
    return decode_string

