#!/usr/bin/python3
"""
Script that safely takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
This script is protected from MySQL injections.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create cursor to execute queries
    cursor = db.cursor()

    # Use parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute query with parameters
    cursor.execute(query, (state_name,))

    # Fetch all rows
    states = cursor.fetchall()

    # Display results
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()
