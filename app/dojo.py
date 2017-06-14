import random
import sys
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ormMethods import *
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
        self.unallocated = {}

    def create_room(self, room_type, room_name):
        if type(room_name) == str:
            if room_type == 'OFFICE':
                # check if room exists
                if room_name not in self.dojo_offices:
                    # create an office
                    new_office = Office(room_name)
                    self.dojo_offices[room_name] = []
                    print('\n\n')
                    print(
                        '\x1b[6;30;42m' + 'A new office called {} has been created'.format(room_name) + '\x1b[0m')
                    print('\n\n')
                    return new_office
                else:
                    print('\n\n')
                    print(
                        '\x1b[6;30;41m' + 'The room {} already exists'.format(room_name) + '\x1b[0m')
                    print('\n\n')

            # if room is living space
            elif room_type == 'LIVINGSPACE':
                # check if room already exists
                if room_name not in self.dojo_livingspaces:
                    new_livingspace = LivingSpace(room_name)
                    self.dojo_livingspaces[room_name] = []
                    print('\n\n')
                    print(
                        '\x1b[6;30;42m' + 'A new living space called {} has been created'.format(room_name) + '\x1b[0m')
                    print('\n\n')
                    return new_livingspace
                else:
                    print('\n\n')
                    print(
                        '\x1b[6;30;41m' + 'The room {} already exists'.format(room_name) + '\x1b[0m')
                    print('\n\n')
            # else
            else:
                # invalid room
                print('\n\n')
                print(
                    '\x1b[6;30;41m' + 'You have entered an invalid room. Please enter office or Livingspace' + '\x1b[0m')
                print('\n\n')
        else:
            print('\n\n')
            print('\x1b[6;30;41m' +
                  'Please enter a valid room name' + '\x1b[0m')
            print('\n\n')

    '''A method that allocates a person to a random office or livingspace'''

    def allocate_random(self, name, room_type, dictionary_type, living_or_office, position):
        try:
            random_room = random.choice(list(dictionary_type))
            if (len(dictionary_type[random_room])) < living_or_office.max_people:
                dictionary_type[random_room].append(name)
                ID = str(id(name))
                print('\n\n')
                print('\x1b[6;30;42m' + '{}(ID:{}) has been allocated the {} {}'.format(
                    name.name, ID, room_type, random_room) + '\x1b[0m')
                print('\n\n')
                self.staff_and_fellows[name] = [
                    random_room, position, room_type]
            else:
                allocate_random(self, name, room_type,
                                dictionary_type, position, living_or_office)
        except:
            if name not in self.unallocated:
                self.unallocated[name] = []
                self.unallocated[name].append(position)
                requirement = 'Needs '+room_type
                self.unallocated[name].append(requirement)
                print('\n\n')
                print('\x1b[6;30;47m' + 'There is no room available at the moment. {}(ID:({})has been added to the unallocated list'.format(
                     name.name, id(name)) + '\x1b[0m')
                print('\n\n')
            else:
                requirement = 'Needs '+room_type
                self.unallocated[name].append(requirement)


    def add_person(self, name, position, wants_accomodation):
        office = 'office'
        livingspace = 'Living space'
        '''A method that allocates a random room'''

        if (position == 'STAFF'):
            # adds a person to the system
            new_staff = Staff(name)
            name = new_staff
            # allocate staff a random room
            self.allocate_random(
                name, office, self.dojo_offices, Office, position)

            if (wants_accomodation == 'Y'):
                print('\n\n')
                print(
                    '\x1b[6;30;41m' + 'Sorry there are no living spaces available for staff' + '\x1b[0m')
                print('\n\n')
            return new_staff

        else:
            # Adds fellow to the system
            new_fellow = Fellow(name)
            name = new_fellow
            # Allocate the fellow a random room
            self.allocate_random(
                name, office, self.dojo_offices, LivingSpace, position)
            if (wants_accomodation == 'Y'):
                self.allocate_random(
                    name, livingspace, self.dojo_livingspaces, LivingSpace, position)
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
            return 'THIS ROOM IS CURRENTLY EMPTY'
        # print print the names in the list seperated by a comma
        for names in self.dojo_offices[name]:
            print(' '+names.name+' ID: '+str(id(names)))
        print('\n')

    def print_room(self, name):
        '''print the key as header'''
        print('\n\n')
        print('\x1b[1;31m'+name+'\x1b[0m')
        '''check if name is in offices'''
        if name in self.dojo_offices:
            self.print_out(self.dojo_offices, name)

        elif name in self.dojo_livingspaces:
            self.print_out(self.dojo_livingspaces, name)

        else:
            print('\x1b[6;30;41m' +
                  'Sorry the room does not exist' + '\x1b[0m')
            return 'Sorry the room does not exist'

    def rooms_allocation(self, type_of_room):
        '''get a list of all the keys'''

        print_allocations_list = []
        for key, value in type_of_room.items():
            print_allocations_list.append(key)
        '''for every key iterate through and print out allocations'''
        for i in range(len(print_allocations_list)):
            print('\n')
            print(print_allocations_list[i])

            print(('_'*50))
            for names in type_of_room[print_allocations_list[i]]:
                print(names.name + ' ID:' + str(id(names)))
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

            print('\x1b[1;31m'+'OFFICE ALLOCATION'+'\x1b[0m')
            self.rooms_allocation(self.dojo_offices)
            print('\x1b[1;31m'+'LIVING SPACE ALLOCATION'+'\x1b[0m')
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
            people = []
            for key, value in self.unallocated.items():
                people.append(key)
            for i in range(len(people)):
                result = ('   '.join(self.unallocated[people[i]])).upper()
                print(people[i].name+'(ID:{}) '.format(id(people[i]))+result)

        else:
            orig_stdout = sys.stdout
            saveFile = open(filename, 'w')
            sys.stdout = saveFile

            print(*('*'*10), sep='-'*9)
            print('\n')

            for key, value in self.unallocated.items():
                print(key+' :'+value)

            sys.stdout = orig_stdout
            saveFile.close()
    def allocate_office_or_living_space(self,room_dicitonary,room_type,room_to_allocate,person_need,person_id):
        # try:
        #     room_dicitonary[room_to_allocate]
        if len(room_dicitonary[room_to_allocate]) < room_type.max_people:
            person_to_remove = []
            for key in self.unallocated.keys():
                if person_id == id(key):
                    if len(self.unallocated[key]) > 2:
                        self.unallocated[key].remove(person_need)
                    else:
                        person_to_remove.append(key)
                    room_dicitonary[room_to_allocate].append(key)
                else:
                    print('Could not find anyone with that ID in the unallocated list. Please try again')
            if len(person_to_remove) > 0:
                self.unallocated.pop(person_to_remove[0])
        else:
            print('Sorry that room is already full. Please try another room')
        # except:
        #     print('Sorry that room doesn\'t exist. Please try another room')

    def allocate_office(self, person_id, room_to_allocate):
        room_dicitonary = self.dojo_offices
        self.allocate_office_or_living_space(room_dicitonary,Office,room_to_allocate,'Needs office',person_id)
        
    def allocate_livingspace(self, person_id, room_to_allocate):
        self.allocate_office_or_living_space(self.dojo_livingspaces,LivingSpace,room_to_allocate,'Needs Living space',person_id)


    def allocate_specific_room(self, new_room, name, old_room, room_type, office):
        try:
            room_type[new_room]
            if len(room_type[new_room]) < office.max_people:
                room_type[new_room].append(name)
                print('\n\n')
                print('\x1b[6;30;42m' + name.name +
                      ' has been moved to '+new_room + '\x1b[0m')
                print('\n\n')
                old_room.remove(name)

            else:
                print('\n\n')
                print('\x1b[6;30;41m' +
                      'Sorry that room is already full' + '\x1b[0m')
                print('\n\n')

        except:
            print('\n\n')
            print(
                '\x1b[6;30;41m' + 'Sorry the room does not exist. Please create the room first' + '\x1b[0m')
            print('\n\n')

    def reallocate_person(self, person_id, new_room, room_type):
        available_rooms = []
        try:
            if room_type == 'OFFICE':
                room_type = self.dojo_offices
                office = Office
            elif room_type == 'LIVINGSPACE':
                room_type = self.dojo_livingspaces
                office = LivingSpace

            for key, value in room_type.items():
                available_rooms.append(key)

            for i in range(len(available_rooms)):
                for name in room_type[available_rooms[i]]:
                    if id(name) == person_id:
                        old_room = room_type[available_rooms[i]]
                        self.allocate_specific_room(
                            new_room, name, old_room, room_type, office)
        except:
            print('Please enter either office or livingspace as the room type')

    def load_people(self, filename):
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

            self.add_person(name, position, wants_accomodation)

    def save_state(self):

        engine = create_engine('sqlite:///offices.db', echo=False)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        def save_state_of_office_or_livingspace(office_or_livingspace, room_type):
            for key, value in office_or_livingspace.items():
                room_name = key
                room = Rooms(room_name, room_type)
                print(room_name+' '+room_type)
                session.add(room)
                session.commit()

        save_state_of_office_or_livingspace(self.dojo_offices, 'OFFICE')
        save_state_of_office_or_livingspace(
            self.dojo_livingspaces, 'LIVING SPACE')

        def save_state_of_assigned_people(office_or_livingspace,room_type):
            rooms = []
            for key, value in office_or_livingspace.items():
                rooms.append(key)
            for i in range(len(rooms)):
                room_list = office_or_livingspace[rooms[i]]
                length_of_room = len(office_or_livingspace[rooms[i]])
                for j in range(length_of_room):
                    name = room_list[j].name
                    position = room_list[j].position
                    room = rooms[i]
                    room_type = room_type
                    print(name+' '+position+' '+room+' '+room_type)
                    people = People(name, position, room, room_type)
                    session.add(people)
                    session.commit()

        save_state_of_assigned_people(self.dojo_offices, 'OFFICE')
        save_state_of_assigned_people(self.dojo_livingspaces, 'LIVING SPACE')


        def save_state_of_unallocated():
            unallocated_people = []
            for key, value in self.unallocated.items():
                unallocated_people.append(key)
            for i in range(len(unallocated_people)):
                name = unallocated_people[i].name
                position = self.unallocated[unallocated_people[i]][0]
                

                if len(self.unallocated[unallocated_people[i]]) > 2:
                    need1 = self.unallocated[unallocated_people[i]][1]
                    need2 = self.unallocated[unallocated_people[i]][2]
                    print(name+' '+position+' '+need1+' '+need2)
                    unallocated = Unallocated(name,position,need1,need2)
                    session.add(unallocated)
                    session.commit()
                else:
                    need1 = self.unallocated[unallocated_people[i]][1]
                    print(name+' '+position+' '+need1)
                    unallocated = Unallocated(name,position,need1,'No need')
                    session.add(unallocated)
                    session.commit()

              
        save_state_of_unallocated()




      

        

    def load_state(self):
        engine = create_engine('sqlite:///offices.db', echo=False)
        # Base.metadata.create_all(engine)
        # create a Session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Create objects
        def load_rooms_and_people(type_of_room):

            for room in session.query(Rooms).order_by(Rooms.id):
                if room.roomtype == 'OFFICE':
                    room_dictionary = self.dojo_offices
                else:
                    room_dictionary = self.dojo_livingspaces
                room_dictionary[room.roomname] = []
                for person in session.query(People).order_by(People.id):
                    if person.room == room.roomname:
                        if person.position == 'STAFF':
                            person = Staff(person.name)
                            room_dictionary[room.roomname].append(person)
                        else:
                            person = Fellow(person.name)
                            room_dictionary[room.roomname].append(person)

        load_rooms_and_people('OFFICE')
        load_rooms_and_people('LIVING SPACE')

        Base.metadata.create_all(engine)
