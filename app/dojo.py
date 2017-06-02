import random
import sys
from office import Office
from livingspace import LivingSpace
from fellow import Fellow
from staff import Staff


class Dojo(object):
    """docstring for Dojo"""

    def __init__(self):

        self.dojo_offices = {}
        self.dojo_livingspaces = {}
        self.staff_and_fellows = {}
        self.unallocated = []


    def create_room(self, room_type, room_name):
        if type(room_name) == str:
            if room_type == 'OFFICE':
                # check if room exists
                if room_name not in self.dojo_offices:
                    # create an office
                    new_office = Office(room_name)
                    self.dojo_offices[room_name] = []
                    print('A new office called {} has been created'.format(room_name))
                    return new_office
                else:
                    print('The room {} already exists'.format(room_name))


            # if room is living space
            elif room_type == 'LIVINGSPACE':
                # check if room already exists
                if room_name not in self.dojo_livingspaces:
                    new_livingspace = LivingSpace(room_name)
                    self.dojo_livingspaces[room_name] = []
                    print(
                        'A new living space called {} has been created'.format(room_name))
                    return new_livingspace
                else:
                    print('The room {} already exists'.format(room_name))
            # else
            else:
                # invalid room
                print(
                    'You have entered an invalid room. Please enter office or Livingspace')
        else:
            print('Please enter a valid room name')

    # A function that allocates a person to a random office
    def allocate_random_office(self, name):
        try:
            random_room = random.choice(list(self.dojo_offices))
            if (len(self.dojo_offices[random_room])) < Office.max_people:
                self.dojo_offices[random_room].append(name)
                print('{} has been allocated the office {}'.format(
                    name, random_room))
                self.staff_and_fellows[name] = random_room
            else:
                self.allocate_random_office(name)
        except:
            self.unallocated.append(name)
            print('There is no room available at the moment. {} has been addedto the unallocated list'.format(name))

    # A function that allocates a person to a random office
    def allocate_random_livingspace(self, name):
        try:
            random_room = random.choice(list(self.dojo_livingspaces))
            if (len(self.dojo_livingspaces[random_room])) < LivingSpace.max_people:
                self.dojo_livingspaces[random_room].append(name)
                print('{} has been allocated the living space {}'.format(
                    name, random_room))
                self.staff_and_fellows[name] = random_room
            else:
                self.allocate_random_room(name)
        except:
            self.unallocated.append(name)
            print('There is no room available at the moment. {} has been addedto the unallocated list'.format(name))

    def add_person(self, name, position, wants_accomodation):
        office = 'office'
        livingspace = 'Living space'
        # A function that allocates a random room

        if (position == 'STAFF'):
            # adds a person to the system
            new_staff = Staff(name)
            
            # allocate staff a random room
            self.allocate_random_office(name)
            
            if (wants_accomodation == 'Y'):
                print('Sorry there are no living spaces available for staff')
            return new_staff

        else:
            # Adds fellow to the system
            new_fellow = Fellow(name)
            self.staff_and_fellows[name] = position
            # Allocate the fellow a random room
            self.allocate_random_office(name)            
            if (wants_accomodation == 'Y'):
                self.allocate_random_livingspace(name)
            return new_fellow

    # A function that prints out a decorator and the members of a room
    def print_out(self, room_to_iterate_through, name):
        # print the decoration
        print('__________________________________________________\n')
        # if the room is empty print out the room is currently empty
        if len(self.dojo_offices[name]) == 0:
            print('THIS ROOM IS CURRENTLY EMPTY')
        # print print the names in the list seperated by a comma
        for names in self.dojo_offices[name]:
            print ' '+names,
        print('\n')

    def print_name(self, name):
        # print the key as header
        print("\n " + name)
        # check if name is in offices
        if name in self.dojo_offices:
            self.print_out(self.dojo_offices, name)

        elif name in self.dojo_livingspaces:
            self.print_out(self.dojo_livingspaces, name)

        else:
            print('Sorry the room does not exist')

    def rooms_allocation(self, type_of_room):
        # get a list of all the keys

        print_allocations_list = []
        for key, value in type_of_room.iteritems():
            print_allocations_list.append(key)
        # for every key iterate through and print out allocations
        for i in range(len(print_allocations_list)):
            print('\n')
            print(print_allocations_list[i])

            print('____________________________________________________\n')
            for names in type_of_room[print_allocations_list[i]]:
                print names,
            print('\n')

    def print_allocations(self, filename):

        if filename == None:

            print('_____________OFFICE ALLOCATION_______________\n')
            self.rooms_allocation(self.dojo_offices)
            print('_____________LIVING SPACE ALLOCATION_________\n')
            self.rooms_allocation(self.dojo_livingspaces)

        else:
            orig_stdout = sys.stdout
            saveFile = open(filename, 'w')
            sys.stdout = saveFile

            print('_____________OFFICE ALLOCATION_______________\n')
            self.rooms_allocation(self.dojo_offices)
            print('_____________LIVING SPACE ALLOCATION_________\n')
            self.rooms_allocation(self.dojo_livingspaces)

            sys.stdout = orig_stdout
            saveFile.close()

    def print_unallocated(self, filename):
        # iterate through the list and print out the names
        # if the user doest request a print out
        if filename == None:
            print(
                '____________________________UNALLOCATED LIST_____________________________')
            print('\n')
    
            for name in (self.unallocated):
                    print name
           
        else:
            orig_stdout = sys.stdout
            saveFile = open(filename, 'w')
            sys.stdout = saveFile

            print(
                '____________________________UNALLOCATED LIST_____________________________')
            print('\n')
            
            for name in (self.unallocated):
                    print name
           

            sys.stdout = orig_stdout
            saveFile.close()

    def get_unique_id(self,name):
        '''
        method generates the unique id which helps the user to reallocate using the id
        '''
        if name in self.staff_and_fellows:

            room = self.staff_and_fellows[name]
            try:
                name_index = self.dojo_livingspaces[room].index(name)
                unique_id = id(room[name_index])
                print('The unique ID for {} is {}'.format(name,unique_id))
            except:
                name_index = self.dojo_offices[room].index(name)
                unique_id = id(room[name_index])
                print('The unique ID for {} is {}'.format(name,unique_id))

        else:
            print('That name doesn\'t exist. Please add the personn first')
