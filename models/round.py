from sqlalchemy import Column, Integer, String
from . import Base


class Round(Base):

    """
    :Example:

    {
    "name": "Quarters Finals",
    "created": "2019-02-18T19:27:41Z",
    "id": 1,
    "modified": "2019-02-18T19:27:41Z",
    "order": 1
    }
    """

    __tablename__ = 'round'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    order = Column(Integer)
