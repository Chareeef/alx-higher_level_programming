#!/usr/bin/python3
'''
Script that prints all City objects from the database hbtn_0e_14_usa
'''


if __name__ == '__main__':

    from model_state import Base, State
    from model_city import City
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

    s = aliased(State, name='s')
    c = aliased(City, name='c')

    results = session.query(s, c).\
            filter(c.state_id == s.id).order_by(c.id).all()

    for (s, c) in results:
        print(f'{s.name}: ({c.id}) {c.name}')
