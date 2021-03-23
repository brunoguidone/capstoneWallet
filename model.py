from sqlalchemy import Column as col
from sqlalchemy import ForeignKey as fk
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship as rel
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = col(Integer, primary_key=True)
    username = col(String(250), nullable=False)
    password = col(String(500), nullable=False)
    email = col(String(250), nullable=False)

    def logged(self):
        return True

    def annonymous(self):
        return False


class Transactions(Base):
    __tablename__ = 'transactions'
    id = col(Integer, primary_key=True)
    user_id = col(Integer, fk('users.id'))
    user = rel(User)


engine = create_engine('postgresql+psycopg2://user:password@hostname/database_name')

Base.metadata.create_all(engine)
