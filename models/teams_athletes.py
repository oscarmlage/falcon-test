from sqlalchemy import Column, Integer, ForeignKey, Table
from . import Base


teams_athletes = Table(
    'teams_athletes', Base.metadata,
    Column('team_id', Integer, ForeignKey('team.id')),
    Column('athlete_id', Integer, ForeignKey('athlete.id')),
    Column('dorsal', Integer)
)
