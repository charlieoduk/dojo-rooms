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

    def room_creator_method(self,room_dictionary,room_type,room_object,room_name):
        ''' A method that creates a new living space or an office. This method is called by the 'create_room'
        method'''

        if room_name not in room_dictionary:
            new_room = room_object(room_name)
            room_dictionary[room_name] = []
            print('\n\n')
            print(
                '\x1b[6;30;42m' + 'A new {} called {} has been created'.format(room_type,room_name) + '\x1b[0m')
            print('\n\n')
            return new_room
        else:
            print('\n\n')
            print(
                '\x1b[6;30;41m' + 'The room {} already exists'.format(room_name) + '\x1b[0m')
            print('\n\n')

    def create_room(self, room_type, room_name):
        '''This method checks the type of room that the user wants to create. The parameters are set depending on
        the type of the room. With the parameters set, it calls the method 'room_creator_method' to create 
        the room'''

        if room_type == 'OFFICE':
            room_dictionary = self.dojo_offices
            room_type = room_type.lower()
            self.room_creator_method(room_dictionary,room_type,Office,room_name)

        elif room_type == 'LIVINGSPACE':
            room_dictionary = self.dojo_livingspaces
            room_type = room_type.lower()
            self.room_creator_method(room_dictionary,room_type,LivingSpace,room_name)
            
        else:
            print('\n\n')
            print(
                '\x1b[6;30;41m' + 'You have entered an invalid room. Please'
                ' enter office or Livingspace' + '\x1b[0m')
            print('\n\n')
        

    

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
            print('\x1b[6;30;42m' + '{}(ID:{}) has been allocated the {} {}'.format(
                name.name, ID, room_type, random_room) + '\x1b[0m')
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
                print('\x1b[6;30;47m' + 'There is no room available at the moment. {}(ID:({})has'
                    ' been added to the unallocated list'.format(
                    name.name, id(name)) + '\x1b[0m')
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
                name, office, self.dojo_offices,Office, position)

            if (wants_accomodation == 'Y'):
                print('\n\n')
                print(
                    '\x1b[6;30;41m' + 'Sorry there are no living spaces available for staff' + '\x1b[0m')
                print('\n\n')
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

        print(('_'*50))
        print('\n')
        if len(room_dictionary[name]) == 0:
            print('THIS ROOM IS CURRENTLY EMPTY')
            print('\n\n')
            
        for names in room_dictionary[name]:
            print(' '+names.name+' ID: '+str(id(names)))
        print('\n')

    def print_room(self, name):
        '''A method that checks if the name of the room to be printed
        as resquested by the user exists. If it does the print_out function is called and 
        the room is printed.'''

        print('\n\n')
        print('\x1b[1;31m'+name+'\x1b[0m')
        
        if name in self.dojo_offices:
            self.print_out(self.dojo_offices, name)

        elif name in self.dojo_livingspaces:
            self.print_out(self.dojo_livingspaces, name)

        else:
            print('\x1b[6;30;41m' +
                  'Sorry the room does not exist' + '\x1b[0m')
            return 'Sorry the room does not exist'

    def rooms_allocation(self, room_dictionary):
        '''A method that finds all the available rooms. The rooms including the members
        are printed ouperson
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

    def print_allocations(self, filename):
        '''A method that prints out all the available rooms as well as the people
        in them. If the user enters a file-name then the list of rooms is printed out to a .txt file.
        If the filename is not specified the rooms are displayed on the command line'''
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
        '''A method that iterates through the unallocated dictionary. prints
        out the name of the people in the dictionary,their position(staff or fellow) and whether
        they need an office or a living space or both.
        '''
        if filename == None:
            print('\n\n')
            print('\x1b[1;31m'+'UNALLOCATED LIST'+'\x1b[0m')
            print(*('*'*10), sep='-'*9)
            print('\n')
            people = []
            for key, value in self.unallocated.items():
                people.append(key)
            for person in range(len(people)):
                result = ('   '.join(self.unallocated[people[person]])).upper()
                print(people[i].name+'(ID:{}) '.format(id(people[person]))+result)

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

    def allocate_office_or_living_space(self, room_dicitonary, room_type, room_to_allocate, person_need, person_id):
        '''A method that allocates a person in the unallocated dictionary to either an offfice or
        a living space that is specified by the user.'''

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
                    print(
                        'Could not find anyone with that ID in the unallocated list. Please try again')
            if len(person_to_remove) > 0:
                self.unallocated.pop(person_to_remove[0])
        else:
            print('Sorry that room is already full. Please try another room')
        # except:
        #     print('Sorry that room doesn\'t exist. Please try another room')

    def allocate_office(self, person_id, room_to_allocate):
        room_dicitonary = self.dojo_offices
        self.allocate_office_or_living_space(
            room_dicitonary, Office, room_to_allocate, 'Needs office', person_id)

    def allocate_livingspace(self, person_id, room_to_allocate):
        self.allocate_office_or_living_space(
            self.dojo_livingspaces, LivingSpace, room_to_allocate, 'Needs Living space', person_id)

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

        def save_state_of_assigned_people(office_or_livingspace, room_type):
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
                    unallocated = Unallocated(name, position, need1, need2)
                    session.add(unallocated)
                    session.commit()
                else:
                    need1 = self.unallocated[unallocated_people[i]][1]
                    print(name+' '+position+' '+need1)
                    unallocated = Unallocated(name, position, need1, 'No need')
                    session.add(unallocated)
                    session.commit()

        save_state_of_unallocated()

    def load_state(self):
        engine = create_engine('sqlite:///offices.db', echo=False)
        # create a Session
        Session = sessionmaker(bind=engine)
        session = Session()
        def load_rooms_and_people_in_them():
            # Load rooms and the respective members of the room
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
            if response == 'Y':
                self.dojo_offices.clear()
                self.dojo_livingspaces.clear()
                load_rooms_and_people_in_them()
                load_unallocated_people()
            elif response == 'N':
                print('You may continue with your current session')
            else:
                print('Please respond with either Y or N')

        Base.metadata.create_all(engine)
