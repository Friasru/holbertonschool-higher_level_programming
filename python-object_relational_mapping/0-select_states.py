#!/usr/bin/env python3
"""
Script to list all states from the hbtn_0e_0_usa database
"""
import pymysql
import sys

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    
    db = pymysql.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=database_name
    )
    
    cursor = db.cursor()
    
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    
    states = cursor.fetchall()
    
    for state in states:
        print(state)
    
    cursor.close()
    db.close()
