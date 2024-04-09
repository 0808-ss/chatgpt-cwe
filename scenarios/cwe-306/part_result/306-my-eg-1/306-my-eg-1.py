from functools import wraps
from flask import abort, Flask, request, redirect, session

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

def ensure_logged_in(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        if 'username' not in session:
            return redirect('/login')
        return f(*args, **kws)
    return decorated_function

# the login page
@app.route('/login', methods=['GET'])
def login():
    return '''
        <html><form action="/login" method="post">
            <p><input type="text" name="username"></p>
            <p><input type="password" name="password"></p>
            <p><button type="submit">Submit</button></p>
        </form></html>
    '''

# the login POST system
@app.route('/login', methods=['POST'])
def do_login():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        session['username'] = request.form['username']
        return redirect('/settings')
    else:
        return 'Bad username or password'

# the home page
@app.route('/')
def index():
    return '''<html>
    Hello! <a href='./login'>Login here</a>
    </html>'''

# user settings page
@app.route('/settings')
@ensure_logged_in
def settings():
    return '''<html>Secret settings</html>'''

if __name__ == '__main__':
    app.run(debug=True)