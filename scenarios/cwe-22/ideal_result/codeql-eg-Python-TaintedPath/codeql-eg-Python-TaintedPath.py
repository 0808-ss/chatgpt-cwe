from flask import Flask, request, redirect, send_from_directory
import os

app = Flask(__name__)

# 设置允许访问的图片文件夹
UPLOAD_FOLDER = 'images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 允许上传的文件扩展名
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/img/<path:filename>')
def img(filename):
    # 获取请求的文件路径
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # 检查请求的文件是否存在于指定的图片文件夹中
    if os.path.isfile(filepath) and os.path.commonpath([os.path.abspath(filepath), os.path.abspath(app.config['UPLOAD_FOLDER'])]) == os.path.abspath(app.config['UPLOAD_FOLDER']):
        # 如果文件存在并且在指定文件夹内，则返回文件
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    else:
        # 否则，返回错误响应或者重定向到其他页面
        return redirect("/")

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    if file and allowed_file(file.filename):
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return 'File uploaded successfully'
    else:
        return 'Invalid file type'