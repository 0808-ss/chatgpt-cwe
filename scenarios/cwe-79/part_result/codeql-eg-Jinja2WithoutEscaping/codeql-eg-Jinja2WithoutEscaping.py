from flask import Flask, request, make_response, escape
from jinja2 import Environment, select_autoescape, FileSystemLoader

app = Flask(__name__)
loader = FileSystemLoader(searchpath="templates/")

# 创建 Jinja2 环境
env = Environment(loader=loader, autoescape=select_autoescape(['html', 'xml']))

def render_response_from_env(env):
    name = escape(request.args.get('name', ''))  # 使用 escape 函数转义用户输入，防止 XSS 攻击
    template = env.get_template('template.html')
    return make_response(template.render(name=name))

# Index page
@app.route('/')
def home():
    return render_response_from_env(env)