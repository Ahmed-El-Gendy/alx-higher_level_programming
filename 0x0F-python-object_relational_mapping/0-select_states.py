#!/usr/bin/python3
"""list states"""
import MySQLdb
from sys import aggv

# The main
if __name__ == '__main__':
    a1 = argv[1]
    a2 = argv[2]
    a3 = argv[3]
    ho = "localhost"
    db = MySQLdb.connect(host=ho, port=3306, user=a1, password=a2, db=a3)

    c = db.cursor()
    c.execute("SELECT * FROM states")
    r = c.fetchall()
    for i in r:
        print(i)
    c.close()
    dp.close()
