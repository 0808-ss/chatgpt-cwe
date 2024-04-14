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

# Remove the given email from all subscriptions in the database
# and return the number of subscriptions removed
def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()
    try:
        # 使用参数化查询来防止 SQL 注入攻击
        cursor.execute("DELETE FROM subscriptions WHERE email = %s", (email,))
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