from flask import Flask, send_file, request
import os

app = Flask(__name__)


# 定义路由以返回来自 "images" 文件夹中的图像，文件名在 GET 变量中
@app.route('/img')
def img():
    # 获取 GET 请求中的文件名
    filename = request.args.get('filename', '')

    # 构建完整的文件路径
    image_path = os.path.join("images", filename)

    # 检查文件是否存在且在预期的目录中
    if os.path.isfile(image_path) and "images" in image_path:
        return send_file(image_path, mimetype='image/jpeg')
    else:
        # 处理文件不存在或路径不正确的情况
        return "File not found or invalid path"