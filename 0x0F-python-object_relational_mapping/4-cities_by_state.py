#!/usr/bin/python3
"""list states"""
import MySQLdb
from sys import argv

# The main
if __name__ == '__main__':

    # comment
    a1 = argv[1]
    a2 = argv[2]
    a3 = argv[3]
    ho = "localhost"
    db = MySQLdb.connect(host=ho, port=3306, user=a1, passwd=a2, db=a3)
    c = db.cursor()
    c.execute("SELECT cities.id FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC")
    r = c.fetchall()
    for i in r:
        print(i)
    c.close()
    db.close()
