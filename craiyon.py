"""
"""

from os import getcwd
from requests import post
from json import loads
from PIL import Image
from io import BytesIO
from base64 import b64decode
from html import escape
from sys import argv

def sendRequest(url, headers, data):
    resp = post(url, headers=headers, data=data)
    return loads(resp.text)['images']

init(convert=True) # Without this, colored text would not work

def image_craiyon(prompt, output_dir='./output/', extension='png'):
    """
    """
    
    illegalChars = '<>:"/\|?*'.join([chr(i) for i in range(32)])
    
    #
    prompt = escape(prompt)
    fileFormat = extension.lower()

    if fileFormat.startswith('.'):
        fileFormat = fileFormat[1:]


    directory = getcwd() + '/' + output_dir

    #
    url = 'https://backend.craiyon.com/generate'
    headers = {'Content-Type': 'application/json'}
    data = f'"prompt": "{prompt}<br>"'
    data = '{' + data + '}'


    response = sendRequest(url, headers, data)

    decoded = []
    i = 0
    for image in response:
        i += 1
        decoded.append(BytesIO(b64decode(image)))

    i = 0
    newPrompt = "creation"
    for image in decoded:
        i += 1
        im = Image.open(image).resize((360, 360))
        fileName = newPrompt + f'-{i}.{fileFormat}'
        output = directory + '/' + fileName 
        im.save(output)

    return output
