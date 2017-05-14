import unittest
from dojo import Dojo
from room import Room


class TestCreateRoom(unittest.TestCase):

    # check if room is created
    def test_create_room_successfully(self):
        kilimanjaro_office = Dojo().create_room("Kilimanjaro", "office")
        self.assertTrue(kilimanjaro_office)
    # check if created toom is an instance of class Room
    def test_create_room_is_instance_of_class_room(self):
        Serengeti_office = Dojo().create_room('Serengeti', 'office')
        self.assertIsInstance(Serengeti_office, Room)
    # Test if maximum capacity of the office is 6
    def test_create_room_max_capacity_of_office_is_six(self):
        Simba_office = Dojo().create_room('Simba', 'office')
        max_number = Simba_office.max_people
        self.assertEqual(max_number, 6)
    # Test if maximum capacity of the living space is 4
    def test_create_room_max_capacity_of_living_space_is_four(self):
        Nzoia_livingspace = Dojo().create_room('Nzoia', 'livingspace')
        max_number = Nzoia_livingspace.max_people
        self.assertEqual(max_number, 4)
    # Test if you can create mutiple rooms
    def test_create_room_check_multiple_rooms_created(self):
        multiple_offices = Dojo.create_room('Kilimanjaro','Serengeti','Nzoia', 'office')
        self.assertTrue(multiple_offices)


