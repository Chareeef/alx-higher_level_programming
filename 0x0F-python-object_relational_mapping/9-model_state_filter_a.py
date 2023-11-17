#!/usr/bin/python3
'''
Script that lists all State objects whose names
contain the letter `a` from the database hbtn_0e_6_usa
'''


if __name__ == '__main__':

    from model_state import Base, State
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
    results = session.query(s).filter(s.name.like('%a%')).order_by(s.id).all()

    for state in results:
        print(f'{state.id}: {state.name}')
