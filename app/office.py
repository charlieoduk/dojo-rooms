from app.room import Room


class Office(Room):
    max_people = 6

    def __init__(self,name):
        self.name = name
        
