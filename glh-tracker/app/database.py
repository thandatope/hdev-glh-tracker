from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import g

from .models import Base


def init_db():
    engine = create_engine("sqlite:///./glh.db")
    Base.metadata.bind = engine
    sess = sessionmaker(bind=engine)
    Base.metadata.create_all()
    s = sess()
    return s


def get_db():
    db = getattr(g, "_db", None)
    if db is None:
        db = g._db = init_db()
    return db
