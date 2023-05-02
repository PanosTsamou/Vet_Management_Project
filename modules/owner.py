from modules.person import *
class Owner(Person):

    def __init__(self,input_first_name, input_last_name, input_dob, input_address, input_email, input_phone_number, input_img = None, input_id = None):
        super().__init__(input_first_name, input_last_name, input_dob, input_address, input_email, input_phone_number, input_img)
        self.id = input_id
        self.list_of_pets= []

    def add_pet(self, pet):
        self.list_of_pets.append(pet)

    def add_id(self, id):
        self.id = int(id)