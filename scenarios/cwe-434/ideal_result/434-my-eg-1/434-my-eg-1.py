from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)


# 保存上传的 PDF 文件到 ./uploads 目录
@app.route('/pdf/upload', methods=['POST'])
def upload_pdf():
    # 检查是否有上传文件
    if 'pdf' not in request.files:
        return "No file provided", 400

    pdf = request.files['pdf']

    # 检查文件名是否以 .pdf 结尾
    if not pdf.filename.lower().endswith('.pdf'):
        return "Invalid file type, only PDF files are allowed", 400

    # 保存文件到 ./uploads 目录
    pdf.save(os.path.join('./uploads', pdf.filename))

    return "File uploaded successfully"


if __name__ == "__main__":
    app.run(debug=True)