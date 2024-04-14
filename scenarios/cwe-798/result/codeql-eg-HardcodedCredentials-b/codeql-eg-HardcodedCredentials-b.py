from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml
import MySQLdb

app = Flask(__name__)

db_host = os.environ["DB_HOST"]
db_user = os.environ["DB_USER"]
db_password = os.environ["DB_PASSWORD"]
db_name = os.environ["DB_NAME"]

# Connect to MySQL database
db = MySQLdb.connect(host=db_host, user=db_user, password=db_password, database=db_name)
cursor = db.cursor()

# Load moderators from database
def load_moderators():
    moderators = {}
    cursor.execute("SELECT username, password FROM moderators")
    results = cursor.fetchall()
    for row in results:
        username = row[0]
        password = row[1]
        moderators[username] = password
    return moderators

# Check if the user is a moderator
def check_mod(username, password):
    moderators = load_moderators()
    if username in moderators and moderators[username] == password:
        return True
    return False

# Route to check if a user is a moderator
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