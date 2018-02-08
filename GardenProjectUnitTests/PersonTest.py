import unittest

from GardenProject.Person import Person

class PersonTest(unittest.TestCase):
    def setUp(self):
        self.person = Person("name")

    def test_rename(self):
        self.assertEqual (self.person.name, "name")

    def test_printUppercased(self):
        self.assertEqual (self.person.printUppercased(), "NAME")

if __name__ == '__main__':
    unittest.main()