#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Using URL construction with minimal string formatting
    url = (
        "mysql+mysqldb://"
        + username
        + ":"
        + password
        + "@localhost/"
        + database
    )
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
