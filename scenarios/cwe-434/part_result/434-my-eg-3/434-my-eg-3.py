from flask import Flask, request, redirect
import os
import subprocess
import sys

app = Flask(__name__)

def file_is_safe_type(file) -> bool:
    return True

#save uploaded files to the folder ./uploads
# if they are safe and if they are less than 2MB
@app.route('/file/upload')

def upload_file():
    if 'f' not in request.files:
        return 'No file part'

    file = request.files['f']

    if file.filename == '':
        return 'No selected file'

    if file and file_is_safe_type(file) and file.content_length < 2 * 1024 * 1024:
        file.save(os.path.join('./uploads', file.filename))
        return 'File uploaded successfully'
    else:
        return 'File upload failed'

@app.route('/file/upload', methods=['POST'])
def file_upload():
    return upload_file()
