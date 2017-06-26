from abc import ABCMeta, abstractmethod

class Room(metaclass=ABCMeta):

    def __init__(self,name):
        self.name = name
