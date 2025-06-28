from sqlalchemy import Column, Integer, String
from .database import Base

class Sensor(Base):
    __tablename__ = "sensors"

    id       = Column(Integer, primary_key=True, index=True)
    name     = Column(String, index=True, nullable=False)
    type     = Column(String, nullable=False)
    location = Column(String, nullable=True)
    unit     = Column(String, nullable=False)
