@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    # Validate username and password inputs
    if not re.match(r'^\w{4,}$', username):
        return "Invalid username format. It must contain at least 4 alphanumeric characters.", 400

    if not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$', password):
        return "Invalid password format. It must contain at least 8 characters including one uppercase letter, one lowercase letter, and one digit.", 400

    try:
        # Hash the password securely using SHA-256
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Connect to MySQL database
        db = MySQLdb.connect(host="your_host",
                             user="your_username",
                             passwd="your_password",
                             db="your_database")

        # Create a cursor object using cursor() method
        cursor = db.cursor()

        # Check if the username already exists in the database
        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        if cursor.fetchone():
            return "Username already exists. Please choose a different one.", 400

        # Insert the new user into the database
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        db.commit()  # Commit the transaction

        return "Registration successful"
    except Exception as e:
        # Handle exceptions, such as database connection errors
        return "Error: " + str(e), 500
    finally:
        # Close the database connection
        db.close()

if __name__ == "__main__":
    app.run(debug=True)