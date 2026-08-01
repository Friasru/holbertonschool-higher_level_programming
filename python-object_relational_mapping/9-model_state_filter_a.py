#!/usr/bin/python3
"""
Script to fetch and display all State objects containing the letter 'a' from the database
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        mysql_user, mysql_password, database_name), pool_pre_ping=True)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
    
    for state in states:
        print("{}: {}".format(state.id, state.name))
    
    session.close()
