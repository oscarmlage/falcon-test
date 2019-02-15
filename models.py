from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import Column, Integer, String, DateTime, func


class BaseModel(object):
    created = Column(DateTime, default=func.now())
    modified = Column(DateTime, default=func.now(), onupdate=func.now())

    @declared_attr
    def __tablename__(self):
        return self.__name__.lower()


Base = declarative_base(cls=BaseModel)


class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    description = Column(String(50))
    created_at = Column(String(50))
    created_by = Column(String(50))
    priority = Column(Integer)
