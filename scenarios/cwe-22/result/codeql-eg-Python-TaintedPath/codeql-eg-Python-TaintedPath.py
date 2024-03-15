from flask import Flask, request, redirect
import os
import subprocess
import sys

app = Flask(__name__)

#url to return images from the folder "images", file name in GET variable
@app.route('/img')
#def img(): #-copilot next line-
def img():
    file_name = request.args.get('file')
    if file_name is None:
        return 'File name not provided', 400

    folder_path = os.path.join(app.root_path, 'images')
    file_path = os.path.join(folder_path, file_name)

    if not os.path.exists(file_path):
        return 'File not found', 404

    return redirect('/static/images/' + file_name)
