from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Match(Base):
    __tablename__ = 'match'
    id = Column(Integer, primary_key=True)
    naverid = Column(String, nullable=False)
    sofascoredid = Column (Integer, nullable=False)
    home = Column(String, nullable=False)
    away = Column(String, nullable=False)
    homeid = Column(Integer, nullable=False)
    awayid = Column(Integer, nullable=False)
    starttime = Column(DateTime, nullable=False)
    
class Player(Base):
    __tablename__ = 'player'
    id = Column(Integer, primary_key=True)
    korname = Column(String, nullable=False)
    sofascoredid = Column(Integer, nullable=False)
    familyname = Column(String, nullable=False)
    
class Nation(Base):
    __tablename__ = 'nation'
    id = Column(Integer, primary_key=True)
    korname = Column(String, nullable=False)
    sofascoredid = Column(Integer, nullable=False)
    
