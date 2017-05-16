import random 
from collections import defaultdict
from office import Office
from livingspace import LivingSpace

class Dojo(object):
    """docstring for Dojo"""
    def __init__(self):

        self.dojo_offices = {}
        self.dojo_livingspaces = {}
        self.staff_and_fellows = {}


    def create_room(self,room_type, room_name):              
        # if isinstance(room_type, str) and isinstance(room_name, str)
        # if type(room_type) == str and type(room_name) == str:
            # if room type is office
        if room_type == 'office':
            # check if room exists
            if room_name not in self.dojo_offices:
                self.dojo_offices[room_name] = []
                print('A new office called {} has been created'.format(room_name))
            else:
                print('The room {} already exists'.format(room_name))
        # if room is living space
        elif room_name == 'livingspace':
            # check if room already exists
            if room_type not in self.dojo_livingspaces:
                self.dojo_livingspaces[room_name] = []
                print('A new living space called {} has been created'.format(room))
            else:
                print('The room {} already exists'.format(room_name))
        # else
        else:
            # invalid room
            print('You have entered an invalid room')
        # else raise value error 
        # else:
            # raise ValueError


    def add_person(self, name, position, wants_accomodation):
        if position == 'STAFF':
            self.staff_and_fellows[name] = 'staff'
            print('Staff {} has been succesfully added'.format(name))
            # adds a person to the system
            # allocates to a random room
            def allocate_random_room():
                random_room = random.choice(list(self.dojo_offices))
                if self.dojo_offices
                self.dojo_offices[random_room].append(name)
                print(self.dojo_offices)
                print(name)
        allocate_random_room()
                
            