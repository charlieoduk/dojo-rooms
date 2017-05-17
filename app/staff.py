from person import Person

class Staff(Person):
	"""docstring for Staff"""
	def __init__(self, arg):
		super(Staff,self).__init__(arg)
		self.arg = arg
		