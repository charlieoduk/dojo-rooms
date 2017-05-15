from office import Office
from livingspace import LivingSpace

class Dojo(object):
    """docstring for Dojo"""
    dojo_offices = {}
    dojo_livingspaces = {}
    staff_and_fellows = {}


    def create_room(room_type, *room_name):        
        # if isinstance(room_type, str) and isinstance(room_name, str)
        if type(room_type) == str and type(room_name) == str:
            # if room type is office
            if room_type == 'office':
                # check if room exists
                if room_type not in dojo_offices:
                    # loop through range in room name to create multiple rooms
                    for room in room_name:
                        new_office = Office(room)
                        dojo_offices[new_office] = []
                        print('A new office called {} has been created'.format(room))
                else:
                    print('The room {} already exists'.format(room_name))
            # if room is living space
            if room_type == 'livingspace':
                # check if room already exists
                if room_type not in dojo_livingspaces:
                    # loop through range in living space to create multiple rooms
                    for room in room_name:
                        new_livingspace = LivingSpace(room)
                        dojo_livingspaces[new_livingspace] = []
                        print('A new living space called {} has been created'.format(room))
                else:
                    print('The room {} already exists'.format(room_name))
            # else
            else:
                # invalid room
                print('You have entered an invalid room')
        # else raise value error 
        else:
            raise ValueError


        def add_person(name, position, wants_accomodation):
            # if name is a string
                # adds a person to the system
                # allocates to a random room

        