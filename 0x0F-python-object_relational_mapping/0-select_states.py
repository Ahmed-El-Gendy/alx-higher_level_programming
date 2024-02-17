#!/usr/bin/python3
import MySQLdb
from sys import aggv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], password=argv[2], db=argv[3])

    c = db.cursor()
    c.execute("SELECT * FROM states")
    r = c.fetchall()
    for i in r:
        print(i)
    c.close()
    dp.close()
