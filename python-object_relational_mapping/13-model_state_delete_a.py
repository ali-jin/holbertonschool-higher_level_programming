#!/usr/bin/python3
"""script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine, delete
from sqlalchemy.orm import Session

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]
    ))

    Base.metadata.create_all(bind=engine)
    session = Session(engine)

    for row in session.query(State).filter(
        State.name.like('%a%')):
        session.delete(row)
    session.commit()
