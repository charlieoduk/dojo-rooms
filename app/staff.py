from person import Person


class Staff(Person):
    """docstring for Staff"""

    def __init__(self, name):
        super(Staff, self).__init__(name)
        self.name = name
