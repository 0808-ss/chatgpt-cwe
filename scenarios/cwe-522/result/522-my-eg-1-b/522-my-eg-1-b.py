from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os

app = Flask(__name__)

#register url
@app.route('/register', methods=['POST'])
def register():
   username = request.form['username']
   password = request.form['password']
   #hash the password
   salt = os.urandom(16)
   hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
   hashed_password = salt + hashed_password

   # Connect to MySQL database
   conn = MySQLdb.connect(host="localhost", user="root", passwd="password", db="mydatabase")
   cursor = conn.cursor()

   # Check if username already exists
   cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
   existing_user = cursor.fetchone()

   if existing_user:
       return "Username already exists!"

   # Insert new user into the database
   cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
   conn.commit()
   conn.close()

   return "Registration successful!"