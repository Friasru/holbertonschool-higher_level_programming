#!/usr/bin/python3
"""
Script to fetch and display a State object by name from the hbtn_0e_6_usa database
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]
    
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        mysql_user, mysql_password, database_name), pool_pre_ping=True)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    state = session.query(State).filter(State.name == state_name).first()
    
    if state is None:
        print("Not found")
    else:
        print(state.id)
    
    session.close()
