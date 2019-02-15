# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


def get_engine(uri):
    return create_engine(uri)


db_session = scoped_session(sessionmaker())
engine = get_engine('sqlite:///stuff.db')


def init_session():
    db_session.configure(bind=engine)

    from models import Base
    Base.metadata.create_all(engine)
