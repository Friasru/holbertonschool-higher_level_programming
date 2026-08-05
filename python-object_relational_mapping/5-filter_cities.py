#!/usr/bin/python3
"""
Script to list all cities of a specific state from the hbtn_0e_4_usa database
"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=database_name
    )

    cursor = db.cursor()

    cursor.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC", (state_name,))

    cities = cursor.fetchall()

    city_names = [city[0] for city in cities]
    print(", ".join(city_names))

    cursor.close()
    db.close()
