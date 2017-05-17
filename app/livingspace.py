from room import Room

class LivingSpace(Room):
    max_people = 4
    def __init__(self,name):
        super(LivingSpace,self).__init__(name)
        self.name = name