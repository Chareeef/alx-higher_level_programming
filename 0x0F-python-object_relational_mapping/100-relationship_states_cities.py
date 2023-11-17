#!/usr/bin/python3
'''
Script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
'''


if __name__ == '__main__':

    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    url = f'mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}'
    engine = create_engine(url)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name='California')

    session.add(california)
    session.commit()

    sanfransisco = City(name='San Francisco', state_id=california.id)
    session.add(sanfransisco)
    session.commit()

    session.close()
