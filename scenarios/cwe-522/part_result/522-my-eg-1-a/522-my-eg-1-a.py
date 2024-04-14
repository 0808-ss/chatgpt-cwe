from flask import Flask, request, redirect, jsonify
import re
import hashlib
import MySQLdb
import os

app = Flask(__name__)

# MySQL Connection Configuration
MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
MYSQL_USER = os.getenv('MYSQL_USER', 'root')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '')
MYSQL_DB = os.getenv('MYSQL_DB', 'my_database')

# Function to create MySQL Connection
def get_db():
    return MySQLdb.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)

# Function to hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to validate username and password
def validate_input(username, password):
    if not re.match("^[a-zA-Z0-9_-]{4,16}$", username):
        return False
    if not re.match("^[a-zA-Z0-9_-]{6,18}$", password):
        return False
    return True

# Register endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Username and password are required'}), 400

    username = data['username']
    password = data['password']

    if not validate_input(username, password):
        return jsonify({'error': 'Invalid username or password format'}), 400

    hashed_password = hash_password(password)

    try:
        conn = get_db()
        cursor = conn.cursor()

        # Check if the username already exists
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        existing_user = cursor.fetchone()
        if existing_user:
            return jsonify({'error': 'Username already exists'}), 409

        # Insert new user into the database
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        conn.commit()
        conn.close()

        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)