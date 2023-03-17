#!/usr/bin/python3
"""script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa"""
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

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    row = session.query(State).filter(State.name == 'Louisiana').first()
    print(row.id)
