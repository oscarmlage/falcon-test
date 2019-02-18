from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

from disciplines_sessions import disciplines_sessions


class Discipline(Base):

    """
    :Example:

    {
    "web": "https://hockey-inline.wrg2019.com/",
    "code": "HI",
    "name": "Hockey Inline",
    "reference": "HI-001",
    "created": "2019-02-18T19:15:31Z",
    "modified": "2019-02-18T19:15:31Z",
    "id": 1
    }
    """

    __tablename__ = 'discipline'
    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    code = Column(String(20))
    web = Column(String(50))
    reference = Column(String(150))

    teams = relationship("Team")

    # Many to Many: sessions
    sessions = relationship(
        "Session",
        secondary=disciplines_sessions,
        back_populates="disciplines"
    )
