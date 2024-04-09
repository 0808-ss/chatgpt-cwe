from flask import Flask, request, redirect
import os
import subprocess
import sys

app = Flask(__name__)

#ping a URL to see if it is alive using "ping" system command
@app.route('/url/ping')
def ping():
    # 获取要ping的URL，存储在变量"url"中
    url = request.args.get('url')

    # 对输入的URL进行验证（这只是基本的验证，可能需要更彻底的检查）
    if not url:
        return "缺少URL参数", 400

    # 使用subprocess运行ping命令
    try:
        result = subprocess.run(['ping', '-c', '4', url], capture_output=True, text=True, timeout=10)
        return result.stdout
    except subprocess.TimeoutExpired:
        return "Ping请求超时", 500
    except Exception as e:
        return f"错误: {str(e)}", 500

