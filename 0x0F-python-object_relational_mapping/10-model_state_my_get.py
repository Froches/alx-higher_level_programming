#!/usr/bin/python3
"""
Script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(engine)
    session = Session()

    data = sys.argv[4]
    state = session.query(State).filter(State.name == data).all()

    if state:
        for data in state:
            print(state.id)
    else:
        print("Not found")
    session.close()
