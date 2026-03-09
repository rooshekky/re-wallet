
from sqlalchemy import Column, Integer, String, Float
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    telegram_id = Column(String)
    username = Column(String)
    wallet_address = Column(String)
    balance_eth = Column(Float, default=0.0)
