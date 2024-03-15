from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

#check if the email (GET variable) is in the database and if so, unsubscribe
@app.route('/unsubscribe') #-copilot next line-
def unsubscribe():
    email = request.args.get('email')

    db = MySQLdb.connect(host='localhost', user='root', passwd='', db='mydatabase')
    cursor = db.cursor()
    
    query = "SELECT * FROM subscribers WHERE email = %s"
    cursor.execute(query, (email,))
    row = cursor.fetchone()

    if row:
        # perform unsubscribe process
        query = "DELETE FROM subscribers WHERE email = %s"
        cursor.execute(query, (email,))
        db.commit()
        db.close()
        return "Unsubscribed successfully."
    else:
        db.close()
        return "Email not found in the database."

@app.route('/unsubscribe', methods=['GET'])
def handle_unsubscribe():
    return unsubscribe()
