#!/usr/bin/python3
"""script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa"""
from sys import argv
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    state = "'" + argv[4] + "'"
    cursor.execute("SELECT cities.name FROM cities\
            INNER JOIN states\
            ON cities.state_id = states.id\
            WHERE states.name = {};".format(state))
    result = cursor.fetchall()

    for idx in range(len(result)):
        if idx < len(result) - 1:
            row = result[idx]
            print(row[0], end=', ')
        else:
            row = result[idx]
            print(row[0], end="")
    print()
