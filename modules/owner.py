from modules.person import *
class Owner(Person):

    def __init__(self,input_first_name, input_last_name, input_dob, input_address, input_email, input_phone_number, input_img = "{{ url_for('static', filename='no_img.png') }}", input_id = None):
        super().__init__(input_first_name, input_last_name, input_dob, input_address, input_email, input_phone_number, input_img)
        self.id = input_id
 


    def add_id(self, id):
        self.id = int(id)