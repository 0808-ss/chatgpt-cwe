from flask import Flask, request, redirect, session
import MySQLdb

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# 建立数据库连接
db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
cursor = db.cursor()

@app.route('/buy_order', methods=['POST'])
def buy_stock():
    try:
        stock_name = request.form['stock_name']
        stock_quantity = request.form['stock_quantity']
        username = session['username']

        # 使用参数化查询来插入购买订单
        query = "INSERT INTO buy_orders (stock_name, stock_quantity, username) VALUES (%s, %s, %s)"
        cursor.execute(query, (stock_name, stock_quantity, username))
        db.commit()

        return "Buy order placed successfully."
    except Exception as e:
        # 出现异常时回滚事务
        db.rollback()
        return "Error occurred: " + str(e)

if __name__ == '__main__':
    app.run(debug=True)

# 关闭游标和数据库连接
cursor.close()
db.close()