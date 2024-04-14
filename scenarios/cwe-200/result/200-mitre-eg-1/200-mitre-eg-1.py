def login():
    username = request.form['username']
    password = request.form['password']
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cursor = db.cursor()

    # Hashing the password for secure storage and comparison
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Query to check if the username and hashed password match
    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    cursor.execute(query, (username, hashed_password))
    user = cursor.fetchone()

    if user:
        # Successful login, redirect to some page
        return redirect('/success')
    else:
        # Failed login, redirect back to login page
        return redirect('/login')