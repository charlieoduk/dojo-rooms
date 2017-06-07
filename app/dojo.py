import random
import sys
import csv
from app.office import Office
from app.livingspace import LivingSpace
from app.fellow import Fellow
from app.staff import Staff


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
                    print('\n\n')
                    print('\x1b[6;30;42m' + 'A new office called {} has been created'.format(room_name) + '\x1b[0m')
                    print('\n\n')
                    return new_office
                else:
                    print('\n\n')
                    print('\x1b[6;30;41m' + 'The room {} already exists'.format(room_name) + '\x1b[0m')
                    print('\n\n')


            # if room is living space
            elif room_type == 'LIVINGSPACE':
                # check if room already exists
                if room_name not in self.dojo_livingspaces:
                    new_livingspace = LivingSpace(room_name)
                    self.dojo_livingspaces[room_name] = []
                    print('\n\n')
                    print('\x1b[6;30;42m' + 'A new office called {} has been created'.format(room_name) + '\x1b[0m')
                    print('\n\n')
                    return new_livingspace
                else:
                    print('\n\n')
                    print('\x1b[6;30;41m' + 'The room {} already exists'.format(room_name) + '\x1b[0m')
                    print('\n\n')
            # else
            else:
                # invalid room
                print('\n\n')
                print('\x1b[6;30;41m' + 'You have entered an invalid room. Please enter office or Livingspace' + '\x1b[0m')
                print('\n\n')
        else:
            print('\n\n')
            print('\x1b[6;30;41m' + 'Please enter a valid room name' + '\x1b[0m')
            print('\n\n')

    '''A method that allocates a person to a random office or livingspace'''
    def allocate_random(self, name, room_type, dictionary_type):
        try:
            random_room = random.choice(list(dictionary_type))
            if (len(dictionary_type[random_room])) < Office.max_people:
                dictionary_type[random_room].append(name)
                print('\n\n')
                print('\x1b[6;30;42m' + '{} has been allocated the {} {}'.format(name,room_type, random_room) + '\x1b[0m')
                print('\n\n')
                self.staff_and_fellows[name] = random_room
            else:
                allocate_random(self, name, room_type, dictionary_type)
        except:
            self.unallocated.append(name)
            print('\n\n')
            print('\x1b[6;30;47m' + 'There is no room available at the moment. {} has been added to the unallocated list'.format(name) + '\x1b[0m')
            print('\n\n')


    def add_person(self, name, position, wants_accomodation):
        office = 'office'
        livingspace = 'Living space'
        '''A method that allocates a random room'''

        if (position == 'STAFF'):
            # adds a person to the system
            new_staff = Staff(name)
            
            # allocate staff a random room
            self.allocate_random(name,office,self.dojo_offices)
            
            if (wants_accomodation == 'Y'):
                print('\n\n')
                print('\x1b[6;30;41m' + 'Sorry there are no living spaces available for staff' + '\x1b[0m')
                print('\n\n')
            return new_staff

        else:
            # Adds fellow to the system
            new_fellow = Fellow(name)
            self.staff_and_fellows[name] = position
            # Allocate the fellow a random room
            self.allocate_random(name,office,self.dojo_offices)            
            if (wants_accomodation == 'Y'):
                self.allocate_random(name,livingspace,self.dojo_livingspaces)
            return new_fellow

    # A function that prints out a decorator and the members of a room
    def print_out(self, room_to_iterate_through, name):
        # print the decoration
        print(('_'*50))
        print('\n')
        # if the room is empty print out the room is currently empty
        if len(self.dojo_offices[name]) == 0:
            print('THIS ROOM IS CURRENTLY EMPTY')
            print('\n\n')
        # print print the names in the list seperated by a comma
        for names in self.dojo_offices[name]:
            print (' '+names)
        print('\n')

    def print_name(self, name):
        '''print the key as header'''
        print('\n\n')
        print('\x1b[1;31m'+name+'\x1b[0m')
        '''check if name is in offices'''
        if name in self.dojo_offices:
            self.print_out(self.dojo_offices, name)

        elif name in self.dojo_livingspaces:
            self.print_out(self.dojo_livingspaces, name)

        else:
            print('\x1b[6;30;41m' + 'Sorry the room does not exist' + '\x1b[0m')

    def rooms_allocation(self, type_of_room):
        '''get a list of all the keys'''

        print_allocations_list = []
        for key, value in type_of_room.items():
            print_allocations_list.append(key)
        '''for every key iterate through and print out allocations'''
        for i in range(len(print_allocations_list)):
            print('\n')
            print(print_allocations_list[i])

            print('____________________________________________________\n')
            for names in type_of_room[print_allocations_list[i]]:
                print (names+ ' ID:' +str(id(names)))
            print('\n')

    def print_allocations(self, filename):

        if filename == None:
            print('\n\n')
            print('\x1b[1;31m'+'OFFICE ALLOCATION'+'\x1b[0m') 
            print(*('*'*10), sep='-'*9)
            self.rooms_allocation(self.dojo_offices)
            print('\x1b[1;31m'+'LIVING SPACE ALLOCATION'+'\x1b[0m') 
            print(*('*'*10), sep='-'*9)
            self.rooms_allocation(self.dojo_livingspaces)
            print('\n\n')

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
        '''iterate through the list and print out the names
         if the user doest request a print out'''
        if filename == None:
            print('\n\n')
            print('\x1b[1;31m'+'UNALLOCATED LIST'+'\x1b[0m') 
            print(*('*'*10), sep='-'*9)
            print('\n')
    
            for name in (self.unallocated):
                    print (name)
            print('\n\n')
           
        else:
            orig_stdout = sys.stdout
            saveFile = open(filename, 'w')
            sys.stdout = saveFile

            print(*('*'*10), sep='-'*9)
            print('\n')
            
            for name in (self.unallocated):
                    print (name)
           

            sys.stdout = orig_stdout
            saveFile.close()

    
    
    def allocate_specific_room(self,new_room,name,old_room):
        try:
            self.dojo_offices[new_room]
            if len(self.dojo_offices[new_room]) < Office.max_people:
                self.dojo_offices[new_room].append(name)
                print('\n\n')
                print('\x1b[6;30;42m' + name+' has been moved to the office'+new_room + '\x1b[0m')
                print('\n\n')
                old_room.remove(name)
            else:
                print('\n\n')
                print('\x1b[6;30;41m' + 'Sorry that room is already full' + '\x1b[0m')
                print('\n\n')
                
        except:
            print('\n\n')
            print('\x1b[6;30;41m' + 'Sorry the room does not exist. Please create the room first' + '\x1b[0m')
            print('\n\n')
            


    def reallocate_person(self,person_id, new_room):
        available_rooms = []
        for key, value in self.dojo_offices.items():
            available_rooms.append(key)
        for i in range(len(available_rooms)):
            for name in self.dojo_offices[available_rooms[i]]:
                if id(name) == person_id:
                    old_room = self.dojo_offices[available_rooms[i]]
                    self.allocate_specific_room(new_room,name,old_room)


    def load_people(self,filename):
        with open(filename) as f:
            data = f.readlines()

        reader = csv.reader(data)
        for row in reader:
            str = row[0]
            nameArr = str.split()
            name = nameArr[0]+' '+nameArr[1]
            position = nameArr[2]
            try:
                wants_accomodation = nameArr[3]
            except:
                wants_accomodation = 'N'

            self.add_person(name,position,wants_accomodation)
        
                    
                    
                    