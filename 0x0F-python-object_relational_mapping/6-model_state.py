#!/usr/bin/python3
"""Start link class to table in database
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine


if __name__ == '__main__':

    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    engine = create_engine(f'mysql+mysqldb://{user}:{passwd}@localhost/{db}',
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
