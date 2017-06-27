import random
import sys
import csv

from termcolor import colored
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Models import *
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
        self.unallocated = {}

    def room_creator_method(self, room_dictionary, room_type, room_object, room_name):
        ''' A method that creates a new living space or an office. This method is called by the 'create_room'
        method'''

        if room_name not in room_dictionary:
            new_room = room_object(room_name)
            room_dictionary[room_name] = []
            print('\n\n')
            print(colored(
                'A new {} called {} has been created'.format(room_type, room_name), 'green'))
            print('\n\n')
            return new_room
        else:
            print('\n\n')
            print(colored(
                'The room {} already exists'.format(room_name), 'red'))
            print('\n\n')

    def create_room(self, room_type, room_name):
        '''This method checks the type of room that the user wants to create. The parameters are set depending on
        the type of the room. With the parameters set, it calls the method 'room_creator_method' to create the room'''

        if room_type == 'OFFICE':
            room_dictionary = self.dojo_offices
            room_type = room_type.lower()
            return self.room_creator_method(
                room_dictionary, room_type, Office, room_name)

        elif room_type == 'LIVINGSPACE':
            room_dictionary = self.dojo_livingspaces
            room_type = room_type.lower()
            return self.room_creator_method(
                room_dictionary, room_type, LivingSpace, room_name)

        else:
            print('\n\n')
            print(colored(
                'You have entered an invalid room. Please'
                ' enter office or Livingspace', 'red'))
            print('\n\n')
            return 'You have entered an invalid room. Please enter office or Livingspace'

    def allocate_random(self, name, room_type, room_dictionary, living_or_office_object, position):
        '''This method checks for all the rooms that have some space then allocates an office or 
        livingspace depending on the user's input. If there is no room available the person is added
        to the unallocated people's dictionary
        This method is called by the add_person method'''
        try:
            rooms_with_space = []
            for key, value in room_dictionary.items():
                if len(room_dictionary[key]) < living_or_office_object.max_people:
                    rooms_with_space.append(key)

            random_room = random.choice(rooms_with_space)

            room_dictionary[random_room].append(name)
            ID = str(id(name))
            print('\n\n')
            print(colored('{}(ID:{}) has been allocated the {} {}'.format(
                name.name, ID, room_type, random_room), 'green'))
            print('\n\n')
            self.staff_and_fellows[name] = [
                random_room, position, room_type]

        except:
            if name not in self.unallocated:
                self.unallocated[name] = []
                self.unallocated[name].append(position)
                requirement = 'Needs '+room_type
                self.unallocated[name].append(requirement)
                print('\n\n')
                print(colored('There is no room available at the moment. {}(ID:({})has'
                              ' been added to the unallocated list'.format(name.name, id(name)), 'red'))
                print('\n\n')
            else:
                requirement = 'Needs '+room_type
                self.unallocated[name].append(requirement)

    def add_person(self, name, position, wants_accomodation):
        '''A method that checks whether the person is staff or a fellow. It then calls
        the method 'allocate_random' to allocate the person a living space or office or both'''
        office = 'office'
        livingspace = 'Living space'

        if (position == 'STAFF'):
            new_staff = Staff(name)
            name = new_staff

            self.allocate_random(
                name, office, self.dojo_offices, Office, position)

            if (wants_accomodation == 'Y'):
                print('\n\n')
                print(
                    colored('Sorry there are no living spaces available for staff', 'red'))
                print('\n\n')
                return 'Sorry there are no living spaces available for staff'
            return new_staff

        else:
            new_fellow = Fellow(name)
            name = new_fellow

            self.allocate_random(
                name, office, self.dojo_offices, Office, position)
            if (wants_accomodation == 'Y'):
                self.allocate_random(
                    name, livingspace, self.dojo_livingspaces, LivingSpace, position)
            return new_fellow

    def print_out(self, room_dictionary, name):
        '''A method that prints out the name of the room as well as the
        members of the room. The method is called by the 'print_room' method '''
        print('\x1b[1;31m'+name+'\x1b[0m')
        print(('_'*50))
        if len(room_dictionary[name]) == 0:
            string = 'THIS ROOM IS CURRENTLY EMPTY'
            print(string)
            print('\n\n')
            return string

        for names in room_dictionary[name]:
            print(' '+names.name+' ID: '+str(id(names)))

    def print_room(self, name):
        '''A method that checks if the name of the room to be printed
        as resquested by the user exists. If it does the print_out function is called and 
        the room is printed.'''
        print('\n\n')
        if name in self.dojo_offices:
            return self.print_out(self.dojo_offices, name)

        elif name in self.dojo_livingspaces:
            return self.print_out(self.dojo_livingspaces, name)

        else:
            print(colored(
                  'Sorry the room does not exist', 'red'))
            return 'Sorry the room does not exist'
        print('\n\n')

    def rooms_allocation(self, room_dictionary):
        '''A method that finds all the available rooms. The rooms including the members
        are printed out
        '''

        available_rooms = []
        for key, value in room_dictionary.items():
            available_rooms.append(key)

        for i in range(len(available_rooms)):
            print('\n')
            print(available_rooms[i])

            print(('_'*50))
            for names in room_dictionary[available_rooms[i]]:
                print(names.name + ' ID:' + str(id(names)))
            print('\n')
        return available_rooms

    def print_allocations(self, filename):
        '''A method that prints out all the available rooms as well as the people
        in them. If the user enters a file-name then the list of rooms is printed out to a .txt file.
        If the filename is not specified the rooms are displayed on the command line'''
        if (len(self.dojo_offices) or len(self.dojo_livingspaces)) > 0:
            if filename == None:
                print('\n\n')
                print('\x1b[1;31m'+'OFFICE ALLOCATION'+'\x1b[0m')
                print(*('*'*10), sep='-'*9)
                self.rooms_allocation(self.dojo_offices)
                print('\x1b[1;31m'+'LIVING SPACE ALLOCATION'+'\x1b[0m')
                print(*('*'*10), sep='-'*9)
                self.rooms_allocation(self.dojo_livingspaces)
                print('\n\n')
                return 'Successfully printed to the screen'

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
                return 'Successfully printed to a txt file'
        else:
            print('\n\n')
            print(colored('There are currently no allocations', 'red'))
            print('\n\n')
            return 'There are currently no allocations'

    def print_unallocated(self, filename):
        '''A method that iterates through the unallocated dictionary. prints
        out the name of the people in the dictionary,their position(staff or fellow) and whether
        they need an office or a living space or both.
        '''
        if len(self.unallocated) > 0:
            if filename == None:
                print('\n\n')
                print('\x1b[1;31m'+'UNALLOCATED LIST'+'\x1b[0m')
                print(*('*'*10), sep='-'*9)
                print('\n')
                people = []
                for key, value in self.unallocated.items():
                    people.append(key)
                for person in range(len(people)):
                    result = ('   '.join(self.unallocated[
                              people[person]])).upper()
                    print(people[person].name +
                          '(ID:{}) '.format(id(people[person]))+result)
                print('\n\n')
                return 'Successfuly printed to the screen'
            else:
                orig_stdout = sys.stdout
                saveFile = open(filename, 'w')
                sys.stdout = saveFile

                print(*('*'*10), sep='-'*9)
                print('\n')

                people = []
                for key, value in self.unallocated.items():
                    people.append(key)
                for person in range(len(people)):
                    result = ('   '.join(self.unallocated[
                              people[person]])).upper()
                    print(people[person].name +
                          '(ID:{}) '.format(id(people[person]))+result)

                sys.stdout = orig_stdout
                saveFile.close()

                return 'Successfully printed to a txt file'
        else:
            print('\n\n')
            print(colored('There are no unallocated people', 'red'))
            print('\n\n')
            return 'There are no unallocated people'

    def allocate_office_or_living_space(self, room_dicitonary, max_people, room_to_allocate, person_need, person_id):
        '''A method that allocates a person in the unallocated dictionary to either an office or
        a living space that is specified by the user.'''

        if len(room_dicitonary[room_to_allocate]) < max_people:
            person_to_remove = []
            for key in self.unallocated.keys():
                if person_id == id(key):
                    person_to_remove.append(key)
                    if len(self.unallocated[key]) > 1:
                        self.unallocated[key].remove(person_need)

                    room_dicitonary[room_to_allocate].append(key)
                    print('\n\n')
                    print(colored('Successfully allocated ' +
                                  key.name+' to '+room_to_allocate, 'green'))
                    print('\n\n')
            if len(person_to_remove) == 0:
                print('\n\n')
                print(colored(
                    'Could not find anyone with that ID in the unallocated list. Please try again', 'red'))
                print('\n\n')
            if (len(self.unallocated[person_to_remove[0]])) < 2:
                self.unallocated.pop(person_to_remove[0])
        else:
            print('\n\n')
            print(
                colored('Sorry that room is already full. Please try another room', 'red'))
            print('\n\n')

    def allocate_office(self, person_id, room_to_allocate):
        room_dicitonary = self.dojo_offices
        self.allocate_office_or_living_space(
            room_dicitonary, Office.max_people, room_to_allocate, 'Needs office', person_id)

    def allocate_livingspace(self, person_id, room_to_allocate):
        self.allocate_office_or_living_space(
            self.dojo_livingspaces, LivingSpace.max_people, room_to_allocate, 'Needs Living space', person_id)

    def allocate_specific_room(self, new_room, name, old_room, room_dicitonary, max_people):
        '''A method that allocates a person to a specific room as specified by the user'''
        try:
            room_dicitonary[new_room]
            if len(room_dicitonary[new_room]) < max_people:
                room_dicitonary[new_room].append(name)
                print('\n\n')
                print_statement = name.name + ' has been moved to '+new_room
                print(colored(print_statement, 'green'))
                print('\n\n')
                print(old_room)
                old_room.remove(name)
                return print_statement

            else:
                print('\n\n')
                print_string = 'Sorry that room is already full'
                print(colored(print_string, 'red'))
                print('\n\n')
                return print_string
        except:
            print('\n\n')
            print(
                colored('Sorry the room does not exist. Please create the room first', 'red'))
            print('\n\n')
            return 'Sorry the room does not exist. Please create the room first'

    def reallocate_person(self, person_id, new_room, room_type):
        '''A method that checks the type of room and then sets the arguments based on the room.
        It then calls the allocate_specific_room method to reallocate the person'''

        available_rooms = []
        try:
            if room_type == 'OFFICE':
                room_dicitonary = self.dojo_offices
                max_people = Office.max_people
            elif room_type == 'LIVINGSPACE':
                room_dicitonary = self.dojo_livingspaces
                max_people = LivingSpace.max_people

            for key, value in room_dicitonary.items():
                available_rooms.append(key)

            for i in range(len(available_rooms)):
                for name in room_dicitonary[available_rooms[i]]:
                    if id(name) == person_id:
                        old_room = room_dicitonary[available_rooms[i]]
                        if available_rooms[i] == new_room:
                            print('\n\n')
                            print(
                                colored('No changes made because you are trying to reallocate to the same room', 'red'))
                            print('\n\n')
                            return 'No changes made because you are trying to reallocate to the same room'
                        else:
                            return self.allocate_specific_room(new_room, name, old_room, room_dicitonary, max_people)

        except:
            print(
                colored('Please enter either office or livingspace as the room type', 'red'))

    def load_people(self, filename):
        '''A method that loads and populates rooms from a .txt file'''
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

    def save_state(self, database_name):
        '''A method that saves all the rooms and memebers in them. It also saves all the 
        people in the unallocated dictionary'''
        if database_name == None:
            os.remove('default.db')
            database = 'default.db'
        else:
            database = database_name+'.db'
        if os.path.isfile(database) and (database != 'default.db'):
            print('\n\n')
            print(colored(
                'That file name already exists in the database. Please choose a different name ', 'red'))
            print('\n\n')
        else:
            engine = create_engine('sqlite:///{}'.format(database), echo=False)
            Base.metadata.create_all(engine)
            Session = sessionmaker(bind=engine)
            session = Session()

            print('\n\n')

            def save_state_of_office_or_livingspace(office_or_livingspace, room_type):
                for key, value in office_or_livingspace.items():
                    room_name = key
                    room = Rooms(room_name, room_type)
                    session.add(room)
                    session.commit()

            save_state_of_office_or_livingspace(self.dojo_offices, 'OFFICE')
            save_state_of_office_or_livingspace(
                self.dojo_livingspaces, 'LIVING SPACE')

            def save_state_of_assigned_people(office_or_livingspace, room_type):
                rooms = []
                for key, value in office_or_livingspace.items():
                    rooms.append(key)

                for room in rooms:
                    people_in_room_list = office_or_livingspace[room]
                    for person in range(len(people_in_room_list)):
                        name = people_in_room_list[person].name
                        position = people_in_room_list[person].position
                        people = People(name, position, room, room_type)
                        session.add(people)
                        session.commit()

            save_state_of_assigned_people(self.dojo_offices, 'OFFICE')
            save_state_of_assigned_people(
                self.dojo_livingspaces, 'LIVING SPACE')

            unallocated_people = []
            for key, value in self.unallocated.items():
                unallocated_people.append(key)
            for person in range(len(unallocated_people)):
                name = unallocated_people[person].name
                position = self.unallocated[unallocated_people[person]][0]

                if len(self.unallocated[unallocated_people[person]]) > 2:
                    need1 = self.unallocated[unallocated_people[person]][1]
                    need2 = self.unallocated[unallocated_people[person]][2]
                    unallocated = Unallocated(name, position, need1, need2)
                    session.add(unallocated)
                    session.commit()
                else:
                    need1 = self.unallocated[unallocated_people[person]][1]
                    unallocated = Unallocated(name, position, need1, 'No need')
                    session.add(unallocated)
                    session.commit()

            print(colored('Current state successfully saved!!', 'green'))
            print('\n\n')
            return 'Current state successfully saved!!'

    def load_state(self, database_name):
        '''A method that loads a previously saved state(rooms and the unallocated people'''
        try:
            engine = create_engine(
                'sqlite:///{}'.format(database_name), echo=False)
            Session = sessionmaker(bind=engine)
            session = Session()

            print('\n\n')
            def load_rooms_and_people_in_them():
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

            def load_unallocated_people():
                for person in session.query(Unallocated).order_by(Unallocated.id):
                    name = person.name
                    position = person.position
                    need1 = person.need_one
                    need2 = person.need_two
                    if need2 == 'No need':
                        if position == 'STAFF':
                            name = Staff(name)
                            self.unallocated[name] = [position, need1]
                        else:
                            name = Fellow(name)
                            self.unallocated[name] = [position, need1]
                    else:
                        if position == 'STAFF':
                            name = Staff(name)
                            self.unallocated[name] = [position, need1, need2]
                        else:
                            name = Fellow(name)
                            self.unallocated[name] = [position, need1, need2]

            if (len(self.dojo_offices) or len(self.dojo_livingspaces)) < 1:
                load_rooms_and_people_in_them()
                load_unallocated_people()
            else:
                response = (input(
                    'Please be advised that loading state will get rid of all your current allocations.'
                    ' Do you want to continue? (Y/N)  ')).upper()
                print('\n\n')
                if response == 'Y':
                    self.dojo_offices.clear()
                    self.dojo_livingspaces.clear()
                    load_rooms_and_people_in_them()
                    load_unallocated_people()

                elif response == 'N':
                    print('You may continue with your current session')

                else:
                    print('Please respond with either Y or N')

            print(
                colored('You have successfully loaded the previously saved state!!!', 'green'))
            print('\n\n')
            return 'You have successfully loaded the previously saved state!!!'

            Base.metadata.create_all(engine)
        except:
            print(
                colored('Please enter the database name in the format \'database.db\'', 'red'))
            print('\n\n')
