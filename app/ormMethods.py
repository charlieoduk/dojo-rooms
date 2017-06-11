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
    spacesleft = Column(Integer)
    roomoccupants = Column(String)

    def __init__(self, roomname, roomtype, spacesleft, roomoccupants):
        self.roomname = roomname
        self.roomtype = roomtype
        self.spacesleft = spacesleft
        self.roomoccupants = roomoccupants

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

class Unallocated(object):

    __tablename__ = "Dojo Unallocated"
    id = Column(Integer,primary_key=True)
    name = Column(String)
    position = Column(String)

    def __init__(self, name, position):
        self.name = name
        self.position = position
        

        






        
        







