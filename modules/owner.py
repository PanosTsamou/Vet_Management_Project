from modules.person import *
class Owner(Person):

    def __ini__(self,input_first_name, input_last_name, input_dob, input_address, input_email, input_phone_number, input_img, input_user_name, input_password):
        super().__init__(input_first_name, input_last_name, input_dob, input_address, input_email, input_phone_number, input_img, input_user_name, input_password)
        list_of_pets= []