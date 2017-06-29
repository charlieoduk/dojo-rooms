from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy import Column,Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Rooms(Base):

    __tablename__ = "Dojo Rooms"

    id = Column(Integer, primary_key=True)
    roomname = Column(String)
    roomtype = Column(String)
    def __init__(self, roomname, roomtype):
        self.roomname = roomname
        self.roomtype = roomtype
    
class People(Base):
    
    __tablename__ = "Dojo People"

    id = Column(Integer,primary_key=True)
    name = Column(String)
    position = Column(String)
    room = Column(String)
    room_type = Column(String)

    def __init__(self, name, position, room, room_type):
        self.name = name
        self.position = position
        self.room = room
        self.room_type = room_type

class Unallocated(Base):

    __tablename__ = "Dojo Unallocated"

    id = Column(Integer,primary_key=True)
    name = Column(String)
    position = Column(String)
    need_one = Column(String)
    need_two = Column(String)

    def __init__(self, name, position, need_one, need_two):
        self.name = name
        self.position = position
        self.need_one = need_one
        self.need_two = need_two