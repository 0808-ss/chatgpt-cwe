import re
from flask import Flask, request, redirect

app = Flask(__name__)

# Define the regular expression to match URLs for example.com domain
rv = re.compile(r'^https?://(?:www\.)?example\.com(?:$|/)')

@app.route('/some/path')
def safe(request):
    target = request.args.get('target', '')
    if rv.match(target):
        return redirect(target)
    else:
        return redirect("/")