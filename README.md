# Example with sanic, asyncpg, sqlalchemy

### Installation
```=sh
pip install -r requirements.txt
```
### Config
```=python
DEBUG = True  # Set to True to live reload server
DATABASE = {
    'host': '<HOST>',
    'user': '<USER>',
    'port': '<PORT>',
    'password': '<PASSWORD>',
    'database': '<DBNAME>'
}
PORT = 5000  # Server port
SECRET = 'something-secret'
WORKERS = 1  # Server workers
```
### Table definition (Need to match model definitaion)
```=sql
-- Example
CREATE TABLE IF NOT EXISTS users (
    username varchar(255) NOT NULL UNIQUE primary key,
    password varchar(255) NOT NULL
);
```
### Model definition (Need to match Table definitaion)
```=python
#  Example
from sqlalchemy import (
    Column, String
)

from sqlalchemy.ext.declarative import declarative_base as Base


class User(Base()):
    __tablename__ = 'users'

    username = Column(String(255), nullable=False, primary_key=True)
    password = Column(String(255), nullable=False)
```
### Start server
```=sh
python app.py
```
