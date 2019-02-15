from sqlalchemy import Column, Integer, String
from . import Base


class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    description = Column(String(50))
    priority = Column(Integer)
