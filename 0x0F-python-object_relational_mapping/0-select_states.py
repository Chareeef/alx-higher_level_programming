#!/usr/bin/python3
'''Script that lists all states from the database hbtn_0e_0_usa'''


if __name__ == '__main__':

    import MySQLdb
    from sys import argv

    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    conn = MySQLdb.connect(host='localhost', port=3306, user=user,
                                passwd=passwd, db=db)
    curr = conn.cursor()

    curr.execute('SELECT * FROM states ORDER BY states.id ASC')

    rows = curr.fetchall()
    for row in rows:
        print(row)
