class Person:

    def __init__(self, input_first_name, input_last_name, input_dob, input_address, input_email, input_phone_number, input_img = None):
        self.first_name = input_first_name
        self.last_name = input_last_name
        self.dob = input_dob
        self.address = input_address
        self.email = input_email
        self.phone_number = input_phone_number
        self.img = input_img

    def full_name(self):
        first = self.first_name.capitalize()
        last = self.last_name.capitalize()
        return f"{first} {last}"

    def initials(self):
        return (f"{self.first_name[0]}{self.last_name[0]}").upper()

