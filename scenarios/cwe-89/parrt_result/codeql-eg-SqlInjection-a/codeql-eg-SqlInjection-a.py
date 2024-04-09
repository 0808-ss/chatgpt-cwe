from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

# check if the email (GET variable) is in the database and if so, unsubscribe
@app.route('/unsubscribe')
def unsubscribe():
    email = request.args.get('email')
    if email:
        try:
            db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
            cursor = db.cursor()
            cursor.execute("DELETE FROM subscriptions WHERE email = %s", (email,))
            db.commit()
            db.close()
            return "Successfully unsubscribed."
        except Exception as e:
            return str(e)
    else:
        return "Email parameter is missing."