from app.person import Person


class Staff(Person):
    """docstring for Staff"""
    position = 'STAFF'
    def __init__(self, name):
        super(Staff, self).__init__(name)
        self.name = name
