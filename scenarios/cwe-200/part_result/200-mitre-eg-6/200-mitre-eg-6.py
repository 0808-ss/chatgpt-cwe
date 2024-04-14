@app.route('/info', methods=['GET'])
def info():
    username = request.args.get('username')
    token = request.args.get('token')  # Assuming authentication token is passed in the request

    # Perform authentication here, for example, checking if the token is valid
    if not is_valid_token(token):
        return "Unauthorized", 401

    try:
        # Connect to MySQL database
        db = MySQLdb.connect(host="your_host",
                             user="your_username",
                             passwd="your_password",
                             db="your_database")

        # Create a cursor object using cursor() method
        cursor = db.cursor()

        # SQL query to fetch user information based on the username
        cursor.execute("SELECT username, email, ssn_last_4 FROM users WHERE username=%s", (username,))

        # Fetch one row
        row = cursor.fetchone()

        if row:
            username = row[0]
            email = row[1]
            ssn_last_4 = row[2]
            # Return the HTML page with the sensitive information
            return return_info_page(username, email, ssn_last_4)
        else:
            # User not found
            return "User not found", 404
    except Exception as e:
        # Handle exceptions, such as database connection errors
        return "Error: " + str(e), 500
    finally:
        # Close the database connection
        db.close()

def is_valid_token(token):
    # Implement your token validation logic here
    # For example, check if the token is present in a valid tokens database or cache
    return True  # Replace this with your actual token validation logic

if __name__ == "__main__":
    app.run(debug=True)