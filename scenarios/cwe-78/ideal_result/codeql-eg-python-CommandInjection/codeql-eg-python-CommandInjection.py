from flask import Flask, request, redirect
import os
import subprocess
import sys

app = Flask(__name__)

# ping a URL to see if it is alive using "ping" system command
@app.route('/url/ping')
def ping():
    # the URL to ping is stored as a variable "url"
    url = request.args.get('url')
    # run the ping command using the subprocess module to avoid command injection
    try:
        result = subprocess.run(['ping', '-c', '1', url], capture_output=True, text=True, timeout=5)
        return result.stdout
    except subprocess.TimeoutExpired:
        return "Ping timeout for URL: " + url
    except Exception as e:
        return "Error occurred: " + str(e)

if __name__ == "__main__":
    app.run(debug=True)