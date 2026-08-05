#!/usr/bin/python3
"""Print all City objects with their State name."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State.name, City.id, City.name) \
        .join(City, State.id == City.state_id) \
        .order_by(City.id) \
        .all()

    for state_name, city_id, city_name in results:
        print(f"{state_name}: ({city_id}) {city_name}")

    session.close()
