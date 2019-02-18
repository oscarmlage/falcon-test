from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

from disciplines_sessions import disciplines_sessions


class Session(Base):

    """
    :Example:

    {
    "code": "SPJW",
    "name": "Short Program Junior Women",
    "reference": "SPJW-001",
    "created": "2019-02-18T19:31:00Z",
    "modified": "2019-02-18T19:31:00Z",
    "time": "18:30:00",
    "date": "2018-07-03",
    "id": 1
    }
    """

    __tablename__ = 'session'
    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    code = Column(String(20))
    reference = Column(String(150))
    date = Column(String(150))
    time = Column(String(150))

    # Many to Many: disciplines
    disciplines = relationship(
        "Discipline",
        secondary=disciplines_sessions,
        back_populates="sessions"
    )
