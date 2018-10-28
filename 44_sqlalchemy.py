#!/usr/bin/env python3

# pip3 install sqlalchemy
# pip3 install mysql-connector-python

# create database python3_test;
# grant all on `python3_test`.* to 'shuaicj'@'localhost' identified by 'secret';

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+mysqlconnector://shuaicj:secret@localhost:3306/python3_test')
Session = sessionmaker(bind=engine)

Base = declarative_base()

# define schema
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True, index=True)
    phone = Column(String(100), nullable=False)

# create table 'user'
Base.metadata.create_all(engine)

def insert(name, phone):
    session = Session()
    user = User(name=name, phone=phone)
    session.add(user)
    session.commit()
    session.close()

def query(name):
    session = Session()
    user = session.query(User).filter(User.name == name).first()
    session.close()
    print('User: id=%s name=%s phone=%s' % (user.id, user.name, user.phone))
    return user

def update(id, phone):
    session = Session()
    user = session.query(User).filter(User.id == id).first()
    user.phone = phone
    session.commit()
    session.close()

def delete(id):
    session = Session()
    user = session.query(User).filter(User.id == id).first()
    session.delete(user)
    session.commit()
    session.close()

if __name__ == '__main__':
    insert(name='admin', phone='000000')
    insert(name='shuaicj', phone='111111')
    admin = query(name='admin')
    me = query(name='shuaicj')
    update(id=me.id, phone='222222')
    query(name='shuaicj')
    delete(id=admin.id)
    delete(id=me.id)

