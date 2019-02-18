from sqlalchemy import Column, Integer, String
from . import Base


class Location(Base):

    """
    :Example:

    {
    "city": "Barcelona",
    "name": "Palau Sant Jordi",
    "reference": "PSJ-001",
    "created": "2019-02-18T19:22:02Z",
    "country": "Spain",
    "modified": "2019-02-18T19:22:02Z",
    "number": null,
    "postal_code": "08038",
    "address": "Passeig Olimpic",
    "id": 1,
    "gps": "43.0317522,-7.5922429"
    }
    """

    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    address = Column(String(20))
    postal_code = Column(String(20))
    number = Column(String(50))
    city = Column(String(50))
    country = Column(String(50))
    gps = Column(String(50))
    reference = Column(String(150))
