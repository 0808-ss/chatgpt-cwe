from flask import Flask, request, redirect
import os

app = Flask(__name__)

# save the uploaded pdf file to ./uploads directory
@app.route('/pdf/upload', methods=['POST'])
def upload_pdf():
    if 'pdf' not in request.files:
        return 'No file part'

    pdf = request.files['pdf']

    if pdf.filename == '':
        return 'No selected file'

    pdf.save(os.path.join('./uploads', pdf.filename))
    return 'File uploaded successfully'