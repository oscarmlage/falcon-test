from sqlalchemy import Column, Integer, String
from . import Base


class Category(Base):

    """
    :Example:

    {
    "code": "JUN",
    "name": "Junior",
    "reference": "",
    "created": "2019-02-18T19:12:43Z",
    "gender": "M",
    "modified": "2019-02-18T19:12:43Z",
    "id": 1,
    "initials": "J"
    }
    """

    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    code = Column(String(20))
    initials = Column(String(20))
    gender = Column(String(10))
    reference = Column(String(150))

    """
    Note: Dunno if, having Disciplines and Sessions, we need Categories for
    something
    """
