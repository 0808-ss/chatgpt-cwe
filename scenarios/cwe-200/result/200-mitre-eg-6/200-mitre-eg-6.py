@app.route('/info', methods=['GET'])
def info():
    # Assuming you have session management implemented to retrieve the username
    # username = session['username']
    # Assuming you have authentication implemented and the username is extracted from the authentication
    username = request.args.get('username')

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
            return "User not found"
    except Exception as e:
        # Handle exceptions, such as database connection errors
        return "Error: " + str(e)
    finally:
        # Close the database connection
        db.close()

if __name__ == "__main__":
    app.run(debug=True)