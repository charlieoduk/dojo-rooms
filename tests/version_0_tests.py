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


class TestCheckClassInheritance(unittest.TestCase):
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


class TestCreateRoom(unittest.TestCase):
    def setUp(self):
        self.the_dojo = Dojo()       
        

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

    


class TestAddPerson(unittest.TestCase):
    def setUp(self):
        self.the_dojo = Dojo()
    
        # check if person is added

    def test_if_person_is_added(self):
        new_person = self.the_dojo.add_person('ANDREW', 'STAFF', 'N')
        self.assertTrue(new_person)


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

class TestPrintRoom(unittest.TestCase):
    def setUp(self):
        self.the_dojo = Dojo()

    # check output when room is empty
    def test_check_output_when_room_is_empty(self):
        self.the_dojo.create_room('OFFICE', 'RED')
        print(self.)
        result = self.the_dojo.print_room('RED')
        self.assertIn(str(result), 'THIS ROOM IS CURRENTLY EMPTY')

    # check output when the room does not exist
    def test_check_output_when_no_room_exists(self):
        result = self.the_dojo.print_room('BLUE')
        print(result)
        self.assertEqual(result, 'Sorry the room does not exist')

    # check that people are added on the printed room



