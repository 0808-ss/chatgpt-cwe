from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml

app = Flask(__name__)

# 从 YAML 文件加载管理员信息
with open('moderators.yaml', 'r') as file:
    moderators = yaml.load(file, Loader=yaml.FullLoader)

# 检查用户是否为管理员的函数
def check_mod(username, password):
    if username in moderators and moderators[username] == password:
        return True
    return False

# 路由用于检查用户是否为管理员
@app.route('/check_mod')
def is_moderator():
    username = request.args.get('username')
    password = request.args.get('password')
    if check_mod(username, password):
        return '您是管理员！'
    else:
        return '您不是管理员。'

if __name__ == '__main__':
    app.run(debug=True)