#!/usr/bin/python3
"""script that prints the first State object from the database hbtn_0e_6_usa"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]
    ))

    Base.metadata.create_all(bind=engine)
    session = Session(engine)

    row = session.query(State).first()
    if row is None:
        print("Nothing")
    print(row.id, end="")
    print(": " + row.name)
