from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

from teams_athletes import teams_athletes


class Team(Base):

    """
    :Example:

    {
    "bio": "Biography of Brazil Inline Roller",
    "name": "Brazil Inline Roller",
    "created": "2019-02-18T19:34:11Z",
    "photo": "path/to/uploads/photos/bra-inline-roller-md5.jpg",
    "modified": "2019-02-18T19:34:11Z",
    "id": 1
    }
    """

    __tablename__ = 'team'
    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    bio = Column(String(20))
    photo = Column(String(50))

    # One to One: countries
    country_id = Column(Integer, ForeignKey("country.id"))

    # One to One: countries
    discipline_id = Column(Integer, ForeignKey("discipline.id"))

    # Many to Many: athletes
    athletes = relationship(
        "Athlete",
        secondary=teams_athletes,
        back_populates="teams"
    )
