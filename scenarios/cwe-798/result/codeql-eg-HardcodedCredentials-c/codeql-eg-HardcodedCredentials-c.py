from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    try:
        # 从环境变量中获取数据库连接信息
        db_host = os.environ["DB_HOST"]
        db_user = os.environ["DB_USER"]
        db_password = os.environ["DB_PASSWORD"]
        db_name = os.environ["DB_NAME"]

        # 连接到MySQL数据库
        connection = MySQLdb.connect(host=db_host, user=db_user, password=db_password, database=db_name)
        return connection
    except Exception as e:
        print("Error while connecting to database:", e)
        return None

if __name__ == "__main__":
    app.run(debug=True)