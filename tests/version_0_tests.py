import unittest
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
        self.office_space = Office()
        self.assertIsInstance(self.office_space, Room)

    # check if living space is instance of room
    def test_livingspace_is_instance_of_room(self):
        self.living_space = LivingSpace()
        self.assertIsInstance(self.living_space,Room)

    # check if fellow is instance of person
    def test_fellow_is_instance_of_person(self):
        self.fellow = Fellow()
        self.assertIsInstance(self.fellow,Person)

    # check if staff is instance of person
    def test_staff_is_instance_of_person(self):
        self.staff = Staff()
        self.assertIsInstance(self.staff, Person)

class TestCreateRoom(unittest.TestCase):

    def setUp(self):
        self.the_dojo = Dojo()
        self.create_room = create_room()

    # check if room is created
    def test_create_room_successfully(self):
        kilimanjaro_office = self.the_dojo.create_room("Kilimanjaro", "office")
        self.assertTrue(self.kilimanjaro_office)
    # check if created toom is an instance of class Room
    def test_create_room_is_instance_of_class_room(self):        
        Serengeti_office = self.the_dojo.create_room('Serengeti', 'office')
        self.assertIsInstance(Serengeti_office, Room)
    # Test if maximum capacity of the office is 6
    def test_create_room_max_capacity_of_office_is_six(self):
        Simba_office = self.the_dojo.create_room('Simba', 'office')
        max_number = self.Simba_office.max_people
        self.assertEqual(max_number, 6)
    # Test if maximum capacity of the living space is 4
    def test_create_room_max_capacity_of_living_space_is_four(self):
        Nzoia_livingspace = self.the_dojo.create_room('Nzoia', 'livingspace')
        max_number = self.Nzoia_livingspace.max_people
        self.assertEqual(max_number, 4)
    # Test if you can create mutiple rooms
    def test_create_room_check_multiple_rooms_created(self):
        multiple_offices = self.the_dojo.create_room('Kilimanjaro','Serengeti','Nzoia', 'office')
        self.assertTrue(self.multiple_offices)


class TestAddPerson(unittest.TestCase):
    def setUp(self):
        self.the_dojo = Dojo()
        self.add_person = add_person()

    # check if person is added
    def test_if_person_is_added(self):
        new_person = self.the_dojo.add_person('Andrew', 'staff')
        self.assertTrue(self.new_person)
    # check if person_name is a string
    def test_if_person_name_is_a_string(self):
        new_person = self.the_dojo.add_person('Simon', 'fellow')
        self.assertIsInstance(new_person, str)
    # check if room is allocated
    def test_if_room_is_allocated_to_staff(self):
        pass

    # check if adding accomodation for staff returns an error
    def test_check_if_adding_accomodation_for_staff_returns_error(self):
        pass

    # add a staff member and check if type of person is staffperson
    def test_add_staff_then_check_if_added_person_is_instance_staff(self):
        pass

    # add fellow who wants accomodation. check if living space is allocated
    def test_check_if_living_space_is_allocated_for_fellow_who_wants_accommodation(self):
        pass

    