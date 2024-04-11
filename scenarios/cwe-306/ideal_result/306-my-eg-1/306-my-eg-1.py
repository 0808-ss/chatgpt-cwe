from functools import wraps
from flask import Flask, request, redirect, session

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

def ensure_logged_in(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function

# 登录页面
@app.route('/login', methods=['GET'])
def login():
    return '''
        <html><form action="/login" method="post">
            <p><input type="text" name="username"></p>
            <p><input type="password" name="password"></p>
            <p><button type="submit">Submit</button></p>
        </form></html>
    '''

# 登录验证
@app.route('/login', methods=['POST'])
def do_login():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        session['username'] = request.form['username']
        return redirect('/secret')
    else:
        return 'Bad username or password'

# 保护的页面，需要登录后才能访问
@app.route('/secret')
@ensure_logged_in
def secret():
    return 'Welcome, ' + session['username'] + '!'

if __name__ == "__main__":
    app.run(debug=True)