#!/usr/bin/python3
'''Script that lists all cities from the database hbtn_0e_4_usa'''


if __name__ == '__main__':

    import MySQLdb
    from sys import argv

    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    conn = MySQLdb.connect(host='localhost', port=3306, user=user,
                           passwd=passwd, db=db)
    cur = conn.cursor()

    query = 'SELECT c.id, c.name, s.name '
    query += 'FROM cities c '
    query += 'JOIN states s ON c.state_id = s.id '
    query += 'ORDER BY c.id'

    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)
