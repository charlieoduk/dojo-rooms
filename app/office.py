from room import Room


class Office(Room):
    max_people = 6

    def __init__(self, name):
        super(Office, self).__init__(name)
        self.name = name
