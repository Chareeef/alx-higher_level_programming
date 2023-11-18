#!/usr/bin/python3
'''
Script that lists all City objects, and their respective State object,
contained in the database hbtn_0e_101_usa
'''


if __name__ == '__main__':

    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker, aliased
    from sys import argv

    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    url = f'mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}'
    engine = create_engine(url)

    Session = sessionmaker(bind=engine)
    session = Session()

    c = aliased(City, name='c')

    cities = session.query(c).order_by(c.id).all()

    for c in cities:
        print(f'{c.id}: {c.name} -> {c.state.name}')

    session.close()
