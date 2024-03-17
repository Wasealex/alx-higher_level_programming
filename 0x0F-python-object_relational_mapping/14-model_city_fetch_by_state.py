#!/usr/bin/python3
"""lists all State objects from the database `hbtn_0e_6_usa`.
"""


from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    for ins in session.query(State, City).filter(State.id == City.state_id):
        print("{}: ({:d}) {}".format(ins.State.name,
                                     ins.City.id,
                                     ins.City.name))
