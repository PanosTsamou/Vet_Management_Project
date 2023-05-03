import unittest
from modules.pet import Pet
from modules.owner import Owner

class PetTest(unittest.TestCase):

    def setUp(self):
        self.pet1= Pet("blacky","12/3/2022",15,"male","dog")
        self.owner2 = Owner("Molly", "Brown", "20/6/2003", "23  Walnut street", "mollyb@gmail.com", "77236734658", "/img/molly")

    def test_name(self):
        self.assertEqual("blacky", self.pet1.name)
    
    def test_dob(self):
        self.assertEqual("12/3/2022", self.pet1.dob)
    
    def test_weight(self):
        self.assertEqual(15, self.pet1.weight)
    
    def test_sex(self):
        self.assertEqual("male", self.pet1.sex)
    
    def test_species(self):
        self.assertEqual("dog", self.pet1.species)
    
    def test_add_owner(self):
        self.pet1.add_owner(self.owner2)
        self.assertEqual("Molly", self.pet1.owner.first_name)
        self.assertEqual("Molly Brown", self.pet1.owner.full_name())

    def test_add_id(self):
        self.pet1.add_id(6)
        self.assertEqual(6, self.pet1.id)

    def test_change_chip_status(self):
        self.pet1.add_id(6)
        self.pet1.add_owner(self.owner2)
        self.pet1.change_chip_status()

        self.assertEqual(True, self.pet1.chipped)
        self.assertEqual("MB6", self.pet1.chip_number)
