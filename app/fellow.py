from app.person import Person


class Fellow(Person):
    """docstring for Fellow"""

    def __init__(self, name):
        super(Fellow, self).__init__(name)
        self.name = name
