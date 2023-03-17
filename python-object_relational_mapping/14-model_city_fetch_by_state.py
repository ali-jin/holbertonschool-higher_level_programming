#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""
from model_state import Base, State
from model_city import City
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]
    ))

    Base.metadata.create_all(bind=engine)
    session = Session(engine)

    results = session.query(State, City).join(City).order_by(City.id).all()
    for row, cit in results:
        print("{}: ({}) {}".format(row.name, cit.id, cit.name))
