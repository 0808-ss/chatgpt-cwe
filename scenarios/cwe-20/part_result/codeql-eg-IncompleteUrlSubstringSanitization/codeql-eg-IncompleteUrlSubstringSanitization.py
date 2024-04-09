from flask import Flask, request, redirect
from urllib.parse import urlparse

app = Flask(__name__)

#redirect users to the URL in the request, but only if the url is for the "example.com" domain
@app.route('/redirect/<path:url>') # 使用 path 参数来接收包含斜杠的 URL 路径
def redirect_to_url(url):
    parsed_url = urlparse(url)
    if parsed_url.netloc == 'example.com': # 检查目标 URL 的域名是否为 example.com
        return redirect(url)
    else:
        return "URL不符合要求，无法重定向"