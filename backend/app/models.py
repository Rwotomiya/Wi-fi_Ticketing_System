from sqlalchemy import Column, Integer, String, DateTime, Float
from database import Base
from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=8, max_length=50)
    email: Optional[str]

class Ticket(BaseModel):
    ticket_type: str
    price: float
    duration: int  # in hours

class TicketModel(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, index=True)
    ticket_type = Column(String)
    price = Column(Float)
    duration = Column(Integer) 

class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    email = Column(String, unique=True, nullable=True)