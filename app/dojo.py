from office import Office
from livingspace import LivingSpace

class Dojo(object):
	"""docstring for Dojo"""
	dojo_offices = []
	dojo_livingspaces = []
	def create_room(self, room_type, *room_name):
		# if isinstance(room_type, str) and isinstance(room_name, str)
		if isinstance(room_type, str) and isinstance(room_name, str):
			# if room type is office
			if room_type == 'office':
				# create an office
					# loop through range in room name to create multiple rooms
					for room in range room_name:
						new_office = Office(room)
						dojo_offices.append(new_office)
			# if room is living space
			if room_type == 'livingspace':
				# create living space
					# loop through range in living space to create multiple rooms
					for room in range room_name:
						new_livingspace = LivingSpace(room)
						dojo_livingspaces.append(new_livingspace)
			# else
		    else:
				# invalid room
				print('You have entered an invalid room')
		# else raise value error 
	    else:
	    	raise ValueError

		