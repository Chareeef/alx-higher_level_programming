#!/usr/bin/python3
'''
Script that lists all State objects, and corresponding City objects,
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

    s = aliased(State, name='s')
    c = aliased(City, name='c')

    states = session.query(s).order_by(s.id).all()

    for st in states:
        print(str(st.id) + ':', st.name)

        for c in st.cities:
            print('\t' + str(c.id) + ':', c.name)

    session.close()
