from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    position = Column(String)
    salary = Column(Integer)
    fantpt = Column(Float)
    value = Column(Float)
    predicted_points = Column(Float)

def init_db():
    engine = create_engine('sqlite:///nfl_dfs.db')
    Base.metadata.create_all(engine)
    return engine

def get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()