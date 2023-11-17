#!/usr/bin/python3
'''
Script that lists the State object with the name
passed as an argument from the database hbtn_0e_6_usa
'''


if __name__ == '__main__':

    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker, aliased
    from sys import argv

    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    state_name = argv[4]

    url = f'mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}'
    engine = create_engine(url)

    Session = sessionmaker(bind=engine)
    session = Session()

    s = aliased(State, name='s')
    state = session.query(s).filter(s.name == state_name).first()

    if state:
        print(f'{state.id}')
    else:
        print('Not found')
