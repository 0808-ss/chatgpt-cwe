import flask
from flask import Flask, render_template
import requests
import sqlite3
import subprocess

from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, World!</p>"

# function which says hello to the user
@app.route("/hello/<username>")
def hello(username):
    # 使用 markupsafe.escape 函数转义用户名
    username = escape(username)
    return f"<p>Hello, {username}!</p>"

if __name__ == "__main__":
    app.run(debug=True)