from sqlalchemy import (
    Column, String, Integer
)

from sqlalchemy.ext.declarative import declarative_base as Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, autoincrement=True, primary_key=True)

    # Authentication Attributes.
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)

    def __repr__(self):
        """ Show user object info. """
        return f'<User: {self.username}>'

    def jsonify(self):
        obj = self.__dict__
        obj.pop('_sa_instance_state')
        return obj
