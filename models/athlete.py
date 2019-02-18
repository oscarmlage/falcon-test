from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from . import Base

from teams_athletes import teams_athletes


class Athlete(Base):

    """
    :Example:

    {
    "bio": "This is the Merys biography",
    "surname": "Poppins",
    "name": "Mery",
    "weight": "60",
    "created": "2019-02-18T19:38:04Z",
    "photo": "path/to/uploads/photos/-merypoppins-md5.jpg",
    "country_id": 1,
    "modified": "2019-02-18T19:38:04Z",
    "birthdate": "2001-01-01T12:12:12Z",
    "height": "160",
    "gender": "W",
    "id": 1,
    "reference": "REF001"
    }
    """

    __tablename__ = 'athlete'
    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    surname = Column(String(150))
    birthdate = Column(DateTime, default=func.now())
    bio = Column(String(200))
    photo = Column(String(150))
    weight = Column(String(50))
    height = Column(String(50))
    gender = Column(String(10))
    reference = Column(String(50))

    # One to One: countries
    country_id = Column(Integer, ForeignKey("country.id"))

    # Many to Many: teams
    teams = relationship(
        "Team",
        secondary=teams_athletes,
        back_populates="athletes"
    )
