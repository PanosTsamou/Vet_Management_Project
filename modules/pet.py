from random import randint
class Pet:

    def __init__(self, input_name, input_dob, input_weight, input_sex, input_species = None, input_breed = None, input_pet_img = None, input_treatment = None, input_chipped = False, input_chip_number = None, input_owner = None, input_veterian = None, input_id = None):
        self.name = input_name
        self.dob = input_dob
        self.weight = input_weight
        self.sex = input_sex
        self.chipped = input_chipped
        self.chip_number = input_chip_number
        self.img = input_pet_img
        self.species = input_species
        self.breed = input_breed
        self.treatment = input_treatment
        self.owner = input_owner
        self.veterian = input_veterian
        self.id = input_id

    
        
    def change_chip_status(self):
        self.chipped = True
        self.chip_number = f'{self.owner.initials()}{self.id}'
    
    def add_treatment(self, treatment):
        self.treatment = treatment

    def add_owner(self,owner):
        self.owner = owner
    def add_veterian(self, veterian):
        self.veterian = veterian
    
    def add_id(self, id):
        self.id = int(id)