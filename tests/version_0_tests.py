import unittest

import sys
import csv

from app.dojo import Dojo
from app.room import Room
from app.office import Office
from app.person import Person
from app.fellow import Fellow
from app.staff import Staff
from app.livingspace import LivingSpace


class TestDojo(unittest.TestCase):
    def setUp(self):
        self.the_dojo = Dojo()
        

    # check if office is instance of room
    def test_office_is_instance_of_room(self):
        self.assertTrue(issubclass(Office, Room))

    # check if living space is instance of room
    def test_livingspace_is_instance_of_room(self):

        self.assertTrue(issubclass(LivingSpace, Room))

    # check if fellow is instance of person
    def test_fellow_is_instance_of_person(self):

      self.assertTrue(issubclass(Fellow, Person))

    # check if staff is instance of person
    def test_staff_is_instance_of_person(self):

       self.assertTrue(issubclass(Staff, Person))


    # check if room is created
    def test_create_room_successfully(self):
        initial_office_count = len(self.the_dojo.dojo_offices)
        kilimanjaro_office = self.the_dojo.create_room("OFFICE", "KILIMANJARO")
        new_office_count = len(self.the_dojo.dojo_offices)
        self.assertEqual((new_office_count - initial_office_count), 1)

    # check if created toom is an instance of class Room
    def test_create_room_is_instance_of_class_room(self):
        Serengeti_office = self.the_dojo.create_room('OFFICE', 'SERENGETI')
        self.assertIsInstance(Serengeti_office, Room)

    # Test if maximum capacity of the office is 6
    def test_create_room_max_capacity_of_office_is_six(self):
        Simba_office = self.the_dojo.create_room('OFFICE', 'SIMBA')
        max_number = Simba_office.max_people
        self.assertEqual(max_number, 6)

    # Test if maximum capacity of the living space is 4
    def test_create_room_max_capacity_of_living_space_is_four(self):
        Nzoia_livingspace = self.the_dojo.create_room('LIVINGSPACE', 'NZOIA')
        max_number = Nzoia_livingspace.max_people
        self.assertEqual(max_number, 4)

    def test_create_room_with_same_name_as_another_room(self):
        self.the_dojo.dojo_offices['RED'] = []
        number_of_rooms = len(self.the_dojo.dojo_offices)
        new_room = self.the_dojo.create_room('OFFICE', 'RED')
        new_number_of_rooms = len(self.the_dojo.dojo_offices)
        self.assertEqual(number_of_rooms, new_number_of_rooms)

        # check if person is added

    def test_if_person_is_added(self):
        new_person = self.the_dojo.add_person('ANDREW', 'STAFF', 'N')
        self.assertTrue(new_person)

    def test_if_office_is_allocated_automatically(self):
        self.the_dojo.dojo_offices['RED'] = []
        number_of_people = len(self.the_dojo.dojo_offices['RED'] )
        self.the_dojo.add_person('LILIAN', 'STAFF', 'N')
        new_number_of_people = len(self.the_dojo.dojo_offices['RED'] )
        self.assertEqual((new_number_of_people - number_of_people),1)

    # check if room is allocated
    def test_if_room_is_allocated_to_staff(self):
        
        office = self.the_dojo.create_room('OFFICE', 'RED')
        initial_person_in_office_count = len(self.the_dojo.dojo_offices['RED'])
        new_person = self.the_dojo.add_person('CHARLES', 'STAFF','N')
        new_person_in_office_count = len(self.the_dojo.dojo_offices['RED'])
        self.assertEqual((new_person_in_office_count - initial_person_in_office_count), 1)

    # check if adding accomodation for staff returns an error
    def test_check_if_adding_accomodation_for_staff_returns_error(self):
        livingspace = self.the_dojo.create_room('LIVINGSPACE', 'RED')
        initial_person_in_living_space_count = len(self.the_dojo.dojo_livingspaces['RED'])
        new_staff_member = self.the_dojo.add_person('WANJIKU', 'STAFF', 'Y')
        new_person_in_livingspace_count = len(self.the_dojo.dojo_livingspaces['RED'])
        self.assertEqual((new_person_in_livingspace_count-initial_person_in_living_space_count),0)

    def test_person_is_added_to_unallocated_if_no_rooms(self):
        unallocated_people = len(self.the_dojo.unallocated)
        self.the_dojo.add_person('CHRIS','STAFF', 'N')
        new_unallocated_people = len(self.the_dojo.unallocated)
        self.assertEqual((new_unallocated_people - unallocated_people),1)

    # add a staff member and check if type of person is staffperson
    def test_add_staff_then_check_if_added_person_is_instance_staff(self):
        new_staff_member = self.the_dojo.add_person('BRENDA', 'STAFF', 'N')
        self.assertIsInstance(new_staff_member, Staff)

    # add fellow who wants accomodation. check if living space is allocated
    def test_check_if_living_space_is_allocated_for_fellow_who_wants_accommodation(self):
        livingspace = self.the_dojo.create_room('LIVINGSPACE', 'RED')
        office = self.the_dojo.create_room('OFFICE', 'BLUE')
        initial_person_in_living_space_count = len(self.the_dojo.dojo_livingspaces['RED'])
        new_fellow = self.the_dojo.add_person('MUNA', 'FELLOW', 'Y')
        new_person_in_livingspace_count = len(self.the_dojo.dojo_livingspaces['RED'])
        self.assertEqual((new_person_in_livingspace_count-initial_person_in_living_space_count),1)

    def test_allocate_office_for_unallocated_person(self):
        unallocated_person = Fellow('JOHN DOE')
        self.the_dojo.unallocated[unallocated_person] = ['FELLOW','NEEDS OFFICE']
        person_id = id(unallocated_person)
        self.the_dojo.create_room('OFFICE', 'RED')
        self.the_dojo.allocate_office(person_id, 'RED')
        self.assertIn(unallocated_person, self.the_dojo.dojo_offices['RED'])

    def test_print_room_with_no_people(self):
        self.the_dojo.create_room('OFFICE', 'RED')
        print_room = self.the_dojo.print_room('RED')
        self.assertEqual(print_room, 'THIS ROOM IS CURRENTLY EMPTY')



    def test_allocate_livingspace_for_unallocated_person(self):
        unallocated_person = Fellow('AWESOME PERSON')
        self.the_dojo.unallocated[unallocated_person] = ['FELLOW','Needs office', 'Needs Living space']
        person_id = id(unallocated_person)
        self.the_dojo.create_room('LIVINGSPACE', 'WHITE')
        self.the_dojo.allocate_livingspace(person_id, 'WHITE')
        self.assertIn(unallocated_person, self.the_dojo.dojo_livingspaces['WHITE'])

    def test_reallocate_person_from_office_to_office(self):
        new_person = Staff('CHARLES ODUK')
        self.the_dojo.dojo_offices['BLUE'] = [new_person]
        self.the_dojo.dojo_offices['RED'] = []

        person_id = id(new_person)
        self.the_dojo.reallocate_person(person_id, 'RED', 'OFFICE')
        self.assertIn(new_person,self.the_dojo.dojo_offices['RED'])

    def test_load_people_from_txt_file(self):
        self.the_dojo.dojo_offices['RED'] = []
        self.the_dojo.dojo_offices['WHITE'] = []
        self.the_dojo.dojo_livingspaces['BLUE'] = []
        self.the_dojo.load_people('sample.txt')
        self.assertTrue((len(self.the_dojo.dojo_offices['RED']) > 0))
        self.assertTrue((len(self.the_dojo.dojo_offices['WHITE']) > 0))
        self.assertTrue((len(self.the_dojo.dojo_livingspaces['BLUE']) > 0))

    def test_load_previously_saved_state(self):
        number_of_offices = len(self.the_dojo.dojo_offices)
        new_number_of_offices = len(self.the_dojo.dojo_offices)










