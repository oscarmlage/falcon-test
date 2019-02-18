from sqlalchemy import Column, Integer, String
from . import Base


class Referee(Base):

    """
    :Example:

    {
    "bio": "Biography of Pier Luiggi Colina",
    "surname": "Colina",
    "name": "Pier Luiggi",
    "created": "2019-02-18T19:25:46Z",
    "photo": "path/to/uploads/photos/pierluiggi-md5.jpg",
    "modified": "2019-02-18T19:25:46Z",
    "birthdate": "1972-01-01T12:12:12Z",
    "gender": "M",
    "id": 1
    }
    """

    __tablename__ = 'referee'
    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    surname = Column(String(150))
    birthdate = Column(String(150))
    bio = Column(String(20))
    photo = Column(String(50))
    gender = Column(String(50))
