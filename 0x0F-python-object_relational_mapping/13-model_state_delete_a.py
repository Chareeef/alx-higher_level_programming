#!/usr/bin/python3
'''
Script that deletes all State objects with a name
containing the letter `a` from the database hbtn_0e_6_usa
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
    la = '%a%'
    session.query(s).filter(s.name.like(la)).delete(synchronize_session=False)
    session.commit()
