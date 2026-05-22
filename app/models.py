from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from .database import Base

class VoluntarioModel(Base):
    __tablename__ = "voluntarios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    fone = Column(String, nullable=False)
    position = Column(String, nullable=False)
    availability = Column(String, nullable=False)
    status = Column(Boolean, default=True) 
    data_inscricao = Column(DateTime, default=datetime.utcnow)