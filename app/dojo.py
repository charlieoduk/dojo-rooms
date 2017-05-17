import random 
import sys
from collections import defaultdict
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

        


    def create_room(self,room_type, room_name):              
        # if isinstance(room_type, str) and isinstance(room_name, str)
        # if type(room_type) == str and type(room_name) == str:
            # if room type is office
        if room_type == 'office':
            # check if room exists
            if room_name not in self.dojo_offices:
                # create an office
                new_office = Office(room_name)
                self.dojo_offices[room_name] = []
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
        

    def allocate_random_office(self,name):
        random_room = random.choice(list(self.dojo_offices))
        if (len(self.dojo_offices[random_room])) < Office.max_people:
            self.dojo_offices[random_room].append(name)
            print('{} has been allocated the office {}'.format(name,random_room))
        else:
            self.allocate_random_office()

    def allocate_random_livingspace(self,name):
        random_room = random.choice(list(self.dojo_livingspaces))
        if (len(self.dojo_livingspaces[random_room])) < LivingSpace.max_people:
            self.dojo_livingspaces[random_room].append(name)
            print('{} has been allocated the living space {}'.format(name,random_room))
        else:
            self.allocate_random_room()




    def add_person(self, name, position, wants_accomodation):
        office ='office'
        livingspace = 'Living space'
        # A function that allocates a random room        

        if (position == 'STAFF'):
            # adds a person to the system
            new_staff = Staff(name)
            self.staff_and_fellows[name] = position            
            # allocate staff a random room
            self.allocate_random_office(name)
            if (wants_accomodation == 'Y'):
                print('Sorry there are no living spaces available for staff')            

        else:
            # Adds fellow to the system
            new_fellow = Fellow(name)
            self.staff_and_fellows[name] = position
            # Allocate the fellow a random room
            self.allocate_random_office(name)
            if (wants_accomodation == 'Y'):
                try:
                    self.allocate_random_livingspace(name)
                except:
                    self.unallocated.append(name)
                    print('There are no rooms available {} added to the unallocated list'.format(name))

      
    def print_name(self, name):        
        # check if name is in offices

        if name in self.dojo_offices:
            # print the key as header
            print(name)
            # print the decoration
            print('__________________________________________________')
            # print print the names in the list seperated by a comma
            for names in self.dojo_offices[name]:
                print(names, )

        elif name in self.dojo_livingspaces:
            # print the key as header
            print(name)
            # print the decoration
            print('__________________________________________________')
            # print print the names in the list seperated by a comma
            for names in self.dojo_livingspaces[name]:
                print(names, )
            
        else:
            print('Sorry the room does not exist')
    def rooms_allocation(self,type_of_room):
        # get a list of all the keys
        
        print_allocations_list = []
        for key, value in type_of_room.iteritems():
            print_allocations_list.append(key)
        # for every key iterate through and print out allocations
        for i in range (len(print_allocations_list)):
            print('\n')
            print(print_allocations_list[i])

            print('____________________________________________________\n')
            for names in type_of_room[print_allocations_list[i]]:
                print names , 
            print('\n')



    def print_allocations(self,filename):
        
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

    def print_unallocated(self,filename)

        

        



            

            
           
     

                
            