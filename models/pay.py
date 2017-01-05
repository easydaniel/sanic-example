from sqlalchemy import (
    Column, String, Integer
)

from sqlalchemy.ext.declarative import declarative_base as Base


class Pay(Base()):
    __tablename__ = 'pays'

    id = Column(Integer, primary_key=True)
    owner = Column(String(255), nullable=False)
    borrower = Column(String(255), nullable=False)
    money = Column(Integer, nullable=False)
