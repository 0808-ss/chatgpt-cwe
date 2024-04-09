from flask import Flask, request, redirect, session
import MySQLdb

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # 设置密钥以启用 session

@app.route('/buy_order', methods=['POST'])
def buy_stock():
    if 'username' not in session:
        return redirect('/login')  # 如果用户未登录，重定向到登录页面

    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']

    try:
        # insert the buy order in the database
        db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
        cursor = db.cursor()
        cursor.execute("INSERT INTO buy_orders (username, stock_name, stock_quantity) VALUES (%s, %s, %s)", (username, stock_name, stock_quantity))
        db.commit()
        db.close()
        return "Buy order placed successfully."
    except Exception as e:
        return str(e)