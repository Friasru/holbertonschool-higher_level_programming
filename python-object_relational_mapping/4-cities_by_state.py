#!/usr/bin/env python3
"""
Script to list all cities from the hbtn_0e_4_usa database with their state names
"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=database_name
    )
    
    cursor = db.cursor()
    
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")
    
    cities = cursor.fetchall()
    
    for city in cities:
        print(city)
    
    cursor.close()
    db.close()
