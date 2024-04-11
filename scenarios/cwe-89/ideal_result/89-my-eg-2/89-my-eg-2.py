#!/bin/python3

from flask import Flask, request, redirect, session
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

# 获取数据库连接
def get_db_connection():
    db = MySQLdb.connect(host="localhost",
                         user="root",
                         passwd="root",
                         db="db")
    return db

# 将用户消息插入数据库
def insert_user_message_in_db(username, message):
    db = get_db_connection()
    cursor = db.cursor()

    try:
        # 使用参数化查询来插入用户消息
        cursor.execute("INSERT INTO user_messages (username, message) VALUES (%s, %s)", (username, message))
        db.commit()
    except Exception as e:
        # 出现异常时回滚事务
        db.rollback()
        print("Error occurred:", str(e))
    finally:
        # 关闭游标和数据库连接
        cursor.close()
        db.close()

@app.route('/post', methods=['POST'])
def post():
    # 从会话中获取用户名
    username = session['username']
    # 从表单中获取消息内容
    message = request.form['message']
    # 插入用户消息到数据库中
    insert_user_message_in_db(username, message)
    return redirect('/')