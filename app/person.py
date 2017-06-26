from abc import ABCMeta, abstractmethod

class Person(metaclass=ABCMeta):

    def __init__(self, name):
        self.name = name
