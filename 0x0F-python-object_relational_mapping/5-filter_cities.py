#!/usr/bin/python3
'''
Script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
'''


if __name__ == '__main__':

    import MySQLdb
    from sys import argv

    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    state_name = argv[4]

    conn = MySQLdb.connect(host='localhost', port=3306, user=user,
                           passwd=passwd, db=db)
    cur = conn.cursor()

    query = 'SELECT c.name '
    query += 'FROM cities c '
    query += 'JOIN states s ON s.id = c.state_id '
    query += 'WHERE s.name = %s '
    query += 'ORDER BY c.id'

    cur.execute(query, (state_name, ))

    cities = cur.fetchall()

    for city in cities:
        print(city[0], end='')
        if (city != cities[-1]):
            print(end=', ')

    print()

    cur.close()
    conn.close()
