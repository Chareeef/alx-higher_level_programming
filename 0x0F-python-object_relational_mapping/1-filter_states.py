#!/usr/bin/python3
'''Script that lists all states with a name starting with N (upper N)'''
import MySQLdb
from sys import argv

user = argv[1]
passwd = argv[2]
db = argv[3]

conn = MySQLdb.connect(host='localhost', port=3306, user=user,
        passwd=passwd, db=db)
curr = conn.cursor()

curr.execute('SELECT * FROM states WHERE name LIKE "N%" ORDER BY states.id ASC')

rows = curr.fetchall()
for row in rows:
    print(row)
