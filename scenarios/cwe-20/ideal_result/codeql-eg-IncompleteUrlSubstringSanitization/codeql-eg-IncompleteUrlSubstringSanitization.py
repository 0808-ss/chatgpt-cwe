from flask import Flask, request, redirect
from urllib.parse import urlparse

app = Flask(__name__)

# 定义路由以重定向用户到请求中的 URL，但仅在 URL 为 "example.com" 域时才允许
@app.route('/redirect/<path:url>')
def redirect_example(url):
    if is_example_domain(url):
        return redirect(url)
    else:
        return redirect("/")

def is_example_domain(url):
    example_domain = "example.com"
    # 解析 URL，获取其域名部分
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    # 检查 URL 的域名是否为 "example.com"
    return domain == example_domain