from modules.person import *

class Veterian(Person):


    def __init__(self,input_first_name, input_last_name, input_dob, input_address, input_email, input_phone_number, input_img, input_id = None):
        super().__init__(input_first_name, input_last_name, input_dob, input_address, input_email, input_phone_number, input_img)
        self.id = input_id
        self.specialization= []

    def add_specialization(self, specialization):
        self.specialization.append(specialization)

    