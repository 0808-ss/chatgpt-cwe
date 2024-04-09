from flask import Flask, request, redirect
from urllib.parse import urlparse

app = Flask(__name__)

# 定义一个函数来验证目标URL是否是 example.com 域
def is_safe_url(target):
    parsed_url = urlparse(target)
    return parsed_url.netloc == 'example.com' and parsed_url.scheme in ('http', 'https')

@app.route('/some/path')
def safe():
    target = request.args.get('target', '')
    if is_safe_url(target):
        return redirect(target)
    else:
        return redirect("/")