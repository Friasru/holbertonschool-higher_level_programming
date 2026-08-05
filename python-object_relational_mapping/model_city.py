#!/usr/bin/python3
"""Defines the City class and links it to the cities table."""

from sqlalchemy import Column, ForeignKey, Integer, String
from model_state import Base


class City(Base):
    """City class mapped to MySQL table cities."""
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
