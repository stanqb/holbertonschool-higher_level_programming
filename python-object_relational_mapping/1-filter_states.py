#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


if __name__ == "__main__":
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

    # Execute query to get states with names starting with N (upper N),
    # sorted by states.id
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    )

    # Fetch all rows
    states = cursor.fetchall()

    # Display results
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()
