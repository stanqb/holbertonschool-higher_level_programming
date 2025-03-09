#!/usr/bin/python3
"""
Module that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


if __name__ == "__main__":
    """
    Script that lists all states from the database hbtn_0e_0_usa
    Takes 3 arguments: mysql username, mysql password and database name
    """
    # Check if all arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

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

    # Execute query to get all states, sorted by states.id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows
    states = cursor.fetchall()

    # Display results
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()
