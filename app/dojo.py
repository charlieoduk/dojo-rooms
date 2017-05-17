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
                # create an office
                new_office = Office(room_name)
                self.dojo_offices[new_office] = []
                print('A new office called {} has been created'.format(room_name))
            else:
                print('The room {} already exists'.format(room_name))
        # if room is living space
        elif room_name == 'livingspace':
            # check if room already exists
            if room_type not in self.dojo_livingspaces:
                new_livingspace = LivingSpace(room_name)
                self.dojo_livingspaces[new_livingspace] = []
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
        office ='office'
        livingspace = 'Living space'
        # A function that allocates a random room
        def allocate_random_room(room_dictionary, type_of_room, max_num_of_people):
            random_room = random.choice(list(room_dictionary))
            if (len(room_dictionary[random_room])) < max_num_of_people:
                room_dictionary[random_room].append(name)
                print('{} has been allocated the {} {}'.format(name,type_of_room, random_room))
            else:
                allocate_random_room(room_dictionary,type_of_room,max_num_of_people)

        if (position == 'STAFF') and (wants_accomodation == 'N'):
            # adds a person to the system
            new_staff = Staff(name)
            self.staff_and_fellows[new_staff] = position            
            # allocate staff a random room
            allocate_random_room(self.dojo_offices,office, Office('Office').max_people)

        elif (position == 'STAFF') and (wants_accomodation == 'Y'):
            print('Sorry there are no living spaces available for staff')

        elif (position == 'FELLOW') and (wants_accomodation == 'N'):
            # Adds fellow to the system
            new_fellow = Fellow(name)
            self.staff_and_fellows[new_fellow] = position
            # Allocate the fellow a random room
            allocate_random_room(self.dojo_offices,office, Office.max_people)        

        else:
            # Adds fellow to the system
            new_fellow = Fellow(name)
            self.staff_and_fellows[new_fellow] = position
            # Allocate the fellow a random room
            allocate_random_room(self.dojo_offices,office, Office.max_people)
            allocate_random_room(self.dojo_livingspaces,livingspace, LivingSpace.max_people)


    def print_name(self, name):
        def print_out(which_dictionary):                
                # print the key as header
                print(name)
                # print the decoration
                print('__________________________________________________')
                # print print the names in the list seperated by a comma
                for names in which_dictionary[name]:
                    print(names, end=', ')
        # check if name is in offices
        if name in self.dojo_offices:
            print_out(self.dojo_offices)
        elif name in self.dojo_livingspaces:
            print_out(self.dojo_livingspaces)
        else:
            print('Sorry the room does not exist')
            

    def print_allocations(self):
        # get a list of all the keys
        print_allocations_list = []
        for key, value in self.dojo_offices:
            print_allocations_list.append(key)
        # for every key iterate through and print out allocations
        for i in range len(print_allocations_list):
            print(self.dojo_offices[print_allocations_list[i]])
            print('____________________________________________________')
            for names in self.dojo_offices[print_allocations_list[i]]:
                print(names, end=', ')




            

            
           
     

                
            