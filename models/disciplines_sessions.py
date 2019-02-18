from sqlalchemy import Column, Integer, ForeignKey, Table
from . import Base


disciplines_sessions = Table(
    'disciplines_sessions', Base.metadata,
    Column('discipline_id', Integer, ForeignKey('discipline.id')),
    Column('session_id', Integer, ForeignKey('session.id')),
    Column('location_id', Integer, ForeignKey('location.id')),
    Column('referee_id', Integer, ForeignKey('referee.id')),
)
