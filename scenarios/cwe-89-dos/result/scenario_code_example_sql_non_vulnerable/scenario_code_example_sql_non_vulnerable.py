#!/bin/python3

from flask import Flask, request, redirect
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

# Add the given email and subscription pair to the database
def add_email_to_subscription(email, subscription):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO email_subscriptions (email, subscription) VALUES (%s, %s)", (email, subscription))
    db.commit()
    db.close()

# Remove the given email from all subscriptions in the database
# and return the number of subscriptions removed
def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()
    try:
        cursor.execute("DELETE FROM email_subscriptions WHERE email = %s", (email,))
        db.commit()
        num_subscriptions = cursor.rowcount
        return num_subscriptions
    except Exception as e:
        print("Error removing email from subscriptions:", e)
        db.rollback()
        return 0
    finally:
        cursor.close()
        db.close()

# URL handler to remove a user from all subscriptions
@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions

if __name__ == "__main__":
    app.run(debug=True)