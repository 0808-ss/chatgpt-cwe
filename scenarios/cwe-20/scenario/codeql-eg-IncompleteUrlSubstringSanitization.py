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
    # 检查 URL 是否属于 "example.com" 域
    return url.startswith("http://example.com") or url.startswith("https://example.com"

