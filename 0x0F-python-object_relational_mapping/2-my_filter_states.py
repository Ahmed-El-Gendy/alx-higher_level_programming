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
    state_name = argv[4]
    ho = "localhost"
    db = MySQLdb.connect(host=ho, port=3306, user=a1, passwd=a2, db=a3)
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE BINARY\
            '{}'".format(state_name))
    r = c.fetchall()
    for i in r:
        print(i)
    c.close()
    db.close()
