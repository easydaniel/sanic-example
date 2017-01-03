from sqlalchemy import (
    Column, String
)

from sqlalchemy.ext.declarative import declarative_base as Base


class User(Base()):
    __tablename__ = 'users'

    # Authentication Attributes.
    username = Column(String(255), nullable=False, primary_key=True)
    password = Column(String(255), nullable=False)
