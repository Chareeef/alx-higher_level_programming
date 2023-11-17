#!/usr/bin/python3
'''Script that lists all State objects from the database hbtn_0e_6_usa'''


if __name__ == '__main__':

    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    engine = create_engine(f'mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}')
    
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State).order_by(State.id).all()

    for state in results:
        print(f'{state.id}: {state.name}')
