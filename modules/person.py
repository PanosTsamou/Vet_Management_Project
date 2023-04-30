class Person:

    def __init__(self, input_first_name, input_last_name, input_dob, input_address, input_email, input_phone_number, input_img, input_user_name = None, input_password = None):
        self.first_name = input_first_name
        self.last_name = input_last_name
        self.dob = input_dob
        self.address = input_address
        self.email = input_email
        self.phone_number = input_phone_number
        self.img = input_img
        self.user_name = input_user_name
        self.password = input_password

    def full_name(self):
        return (f"{self.first_name} {self.last_name}").capitalize()

    def initials(self):
        return (f"{self.first_name[0]}{self.last_name[0]}").upper()

    def username_password_verification(self, username, password):
        if username == self.user_name and password == self.password:
            return True
        else:
            return False