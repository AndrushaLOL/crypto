from db import Base
from sqlalchemy import Column, Integer, String, DateTime, Float
import datetime


class Ticker(Base):
    __tablename__ = 'tickers'
    id = Column(Integer, primary_key=True)
    symbol = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.now)
    open = Column(Float)
    close = Column(Float)
    high = Column(Float)
    low = Column(Float)
    volume = Column(Float)

    def __repr__(self):
        return f'<Ticker(id={self.id}, volume={self.volume}>'
