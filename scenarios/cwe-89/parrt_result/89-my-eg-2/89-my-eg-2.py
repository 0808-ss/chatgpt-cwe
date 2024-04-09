from flask import Flask, request, redirect, session
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host="localhost",
                         user="root",
                         passwd="root",
                         db="db")
    return db

def insert_user_message_in_db(username, message):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO user_messages (username, message) VALUES (%s, %s)", (username, message))
    db.commit()
    db.close()

@app.route('/post', methods=['POST'])
def post():
    if 'username' not in session:
        return redirect('/login')  # 如果用户未登录，重定向到登录页面

    username = session['username']
    message = request.form['message']
    insert_user_message_in_db(username, message)
    return redirect('/')