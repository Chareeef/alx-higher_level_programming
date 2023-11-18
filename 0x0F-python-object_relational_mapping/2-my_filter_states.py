#!/usr/bin/python3
'''
Script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
'''


if __name__ == '__main__':

    import MySQLdb
    from sys import argv

    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    name = argv[4]

    conn = MySQLdb.connect(host='localhost', port=3306, user=user,
                                passwd=passwd, db=db)
    cur = conn.cursor()

    cur.execute('SELECT * FROM states ' +
                'WHERE name LIKE BINARY "{}" '.format(name) +
                'ORDER BY id ASC')

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
