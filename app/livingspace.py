from room import Room

class LivingSpace(Room):
    max_people = 4
    def __init__(self,name):
        super().__init__()
        self.name = name