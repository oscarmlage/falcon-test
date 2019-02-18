from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base


class Country(Base):

    """
    :Example:

    {
    "code": "BR",
    "name": "Brazil",
    "reference": "BRA001",
    "created": "2019-02-18T19:10:19Z",
    "initials": "B",
    "modified": "2019-02-18T19:10:19Z",
    "id": 1
    }
    """

    __tablename__ = 'country'
    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    code = Column(String(20))
    initials = Column(String(20))
    reference = Column(String(150))

    athletes = relationship("Athlete")
    teams = relationship("Team")
