#!/usr/bin/python3
"""a script that lists all City objects from the database hbtn_0e_101_usa
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for obj in session.query(State).order_by(State.id):
        for city_obj in obj.cities:
            print(city_obj.id, city_obj.name, sep=": ", end="")
            print(" -> " + obj.name)
