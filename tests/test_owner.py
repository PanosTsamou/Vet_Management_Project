import unittest
from modules.owner import Owner

class OwenerTests(unittest.TestCase):

    def setUp(self):
        self.owner1 = Owner("Dave", "Bard", "12/3/2000", "23 Long street", "daveb@gmail.com", "77236767398", "/img/dave")
        self.owner2 = Owner("Molly", "Brown", "20/6/2003", "23  Walnut street", "mollyb@gmail.com", "77236734658", "/img/molly")


    def test_get_first_neme1(self):
        self.assertEqual("Dave", self.owner1.first_name)
    
    def test_get_last_neme1(self):
        self.assertEqual("Bard", self.owner1.last_name)
    
    def test_get_dob1(self):
        self.assertEqual( "12/3/2000", self.owner1.dob)
    
    def test_get_address1(self):
        self.assertEqual("23 Long street", self.owner1.address)
    
    def test_get_email1(self):
        self.assertEqual("daveb@gmail.com", self.owner1.email)
    
    
    def test_get_phone_number1(self):
        self.assertEqual("77236767398", self.owner1.phone_number)
    
    def test_get_img1(self):
        self.assertEqual("/img/dave", self.owner1.img)
    
    def test_get_id1(self):
        self.owner1.add_id(3)
        self.assertEqual(3, self.owner1.id)

    def test_get_full_name1(self):
        self.assertEqual("Dave Bard", self.owner1.full_name())
    def test_get_initials1(self):
        self.assertEqual("DB", self.owner1.initials())

    def test_get_first_neme2(self):
        self.assertEqual("Molly", self.owner2.first_name)
    
    def test_get_last_neme2(self):
        self.assertEqual("Brown", self.owner2.last_name)
    
    def test_get_dob2(self):
        self.assertEqual( "20/6/2003", self.owner2.dob)
    
    def test_get_address2(self):
        self.assertEqual("23  Walnut street", self.owner2.address)
    
    def test_get_email2(self):
        self.assertEqual("mollyb@gmail.com", self.owner2.email)
    
    
    def test_get_phone_number2(self):
        self.assertEqual("77236734658", self.owner2.phone_number)
    
    def test_get_img2(self):
        self.assertEqual("/img/molly", self.owner2.img)
    
    def test_get_id2(self):
        self.owner2.add_id(3)
        self.assertEqual(3, self.owner2.id)

    def test_get_full_name2(self):
        self.assertEqual("Molly Brown", self.owner2.full_name())

    def test_get_initials2(self):
        self.assertEqual("MB", self.owner2.initials())
