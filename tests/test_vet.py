import unittest

from modules.vet import Veterian


class VetTest(unittest.TestCase):

    def setUp(self):
        self.veterian1 = Veterian("Aaron", "McCurdy", "2/7/1983", "3  Walnut street", "aaronmc@gmail.com", "77232437169", "/img/aaron")

    def test_get_first_neme(self):
        self.assertEqual("Aaron", self.veterian1.first_name)
    
    def test_get_last_neme2(self):
        self.assertEqual("McCurdy", self.veterian1.last_name)
    
    def test_get_dob2(self):
        self.assertEqual( "2/7/1983", self.veterian1.dob)
    
    def test_get_address2(self):
        self.assertEqual("3  Walnut street", self.veterian1.address)
    
    def test_get_email2(self):
        self.assertEqual("aaronmc@gmail.com", self.veterian1.email)
    
    
    def test_get_phone_number2(self):
        self.assertEqual("77232437169", self.veterian1.phone_number)
    
    def test_get_img2(self):
        self.assertEqual("/img/aaron", self.veterian1.img)
    
    def test_get_id2(self):
        self.veterian1.add_id(5)
        self.assertEqual(5, self.veterian1.id)

    def test_get_full_name2(self):
        self.assertEqual("Aaron Mccurdy", self.veterian1.full_name())

    def test_get_initials2(self):
        self.assertEqual("AM", self.veterian1.initials())
