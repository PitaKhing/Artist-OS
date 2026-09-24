from sqlalchemy import Column, Integer, String
from database import Base

class Release(Base):
    __tablename__ = "releases"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    status = Column(String, nullable=False)