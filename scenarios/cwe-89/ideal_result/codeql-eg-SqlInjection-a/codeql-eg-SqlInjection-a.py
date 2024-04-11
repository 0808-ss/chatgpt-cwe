from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 配置数据库连接信息，这里使用SQLite作为示例数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# 定义订阅者数据模型
class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

# 定义取消订阅路由
@app.route('/unsubscribe')
def unsubscribe():
    # 从 GET 请求中获取邮箱地址
    email = request.args.get('email')

    if email:
        # 查询数据库中是否存在匹配的订阅者
        subscriber = Subscriber.query.filter_by(email=email).first()
        if subscriber:
            # 如果存在，执行取消订阅操作
            db.session.delete(subscriber)
            db.session.commit()
            return "Unsubscribed successfully."
        else:
            return "Email not found in the database."
    else:
        return "Email parameter is missing."

if __name__ == "__main__":
    # 创建数据库表格（如果不存在）
    db.create_all()
    app.run(debug=True)