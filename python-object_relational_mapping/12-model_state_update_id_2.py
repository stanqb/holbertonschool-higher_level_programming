#!/usr/bin/python3
"""
Script that changes the name of a State object from the database hbtn_0e_6_usa
Changes the name of the State where id = 2 to "New Mexico"
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine to connect to MySQL server
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query the State object with id = 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # Update the name if the state exists
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Close session
    session.close()
