from modules.owner import Owner
from modules.vet import Veterian
from modules.pet import Pet
from modules.care import Care
from modules.species import Species
from modules.specialization import Specialization
from modules.appointment import Appointment
 
import repositories.appointment_repository as appoint_repo
import repositories.specialization_repository as spec_repo
import repositories.species_repository as species_repo
import repositories.owner_repository as owner_repo
import repositories.veterian_repository as vet_repo
import repositories.pet_repository as pet_repo
import repositories.care_repository as care_repo

appoint_repo.delete_all()
care_repo.delete_all()
spec_repo.delete_all()
pet_repo.delete_all()
species_repo.delete_all()
vet_repo.delete_all()
owner_repo.delete_all()

species1 = Species('Dog')
species_repo.add_species(species1)
species2 = Species('Cat')
species_repo.add_species(species2)
species3 = Species('Rabbit')
species_repo.add_species(species3)
species4 = Species('Hamster')
species_repo.add_species(species4)
species5 = Species('Guinea pig')
species_repo.add_species(species5)
species6 = Species('Pig')
species_repo.add_species(species6)
species7 = Species('Chicken')
species_repo.add_species(species7)
species8 = Species('Lizards')
species_repo.add_species(species8)
species9 = Species('Turtle')
species_repo.add_species(species9)
owner1 = Owner("Dave", "Bard", "12/3/2000", "23 Long street", "daveb@gmail.com", "77236767398", "/img/dave")
owner_repo.add_owner(owner1)
owner2 = Owner("Molly", "Brown", "20/6/2003", "23  Walnut street", "mollyb@gmail.com", "77236734658", "/img/molly")
owner_repo.add_owner(owner2)
veterian1 = Veterian("Aaron", "McCurdy", "2/7/1983", "3  Walnut street", "aaronmc@gmail.com", "77232437169", "/img/aaron")
vet_repo.add_veterian(veterian1)
veterian2 = Veterian("Patric", "Coile", "15/10/1995", "20 Mary Crescent", "patickc@gmail.com", "77232384933", "/img/patric")
vet_repo.add_veterian(veterian2)

pet1= Pet("blacky","12/3/2022",15,"male",species1)
pet1.add_owner(owner1)
pet_repo.add_pet(pet1)
pet2= Pet("fatty","12/3/2022",60,"male",species1)
pet2.add_owner(owner1)
pet_repo.add_pet(pet2)
pet3= Pet("flafy","12/3/2022",3,"male",species3)
pet3.add_owner(owner2)
pet_repo.add_pet(pet3)
pet4= Pet("margaret","12/3/2022",3,"female",species2)
pet4.add_owner(owner2)
pet_repo.add_pet(pet4)

care1 = Care(pet1, veterian1)
care_repo.add_care(care1)
care2 = Care(pet2, veterian1)
care_repo.add_care(care2)
care3 = Care(pet3, veterian1)
care_repo.add_care(care3)
care4 = Care(pet4, veterian2)
care_repo.add_care(care4)


spec1 = Specialization(species1, veterian1)
spec_repo.add_specialization(spec1)
spec2 = Specialization(species2, veterian1)
spec_repo.add_specialization(spec2)
spec3 = Specialization(species3, veterian1)
spec_repo.add_specialization(spec3)
spec4 = Specialization(species6, veterian1)
spec_repo.add_specialization(spec4)
spec5 = Specialization(species7, veterian1)
spec_repo.add_specialization(spec5)
spec6 = Specialization(species4, veterian2)
spec_repo.add_specialization(spec6)
spec7 = Specialization(species5, veterian2)
spec_repo.add_specialization(spec7)
spec8 = Specialization(species6, veterian2)
spec_repo.add_specialization(spec8)
spec9 = Specialization(species7, veterian2)
spec_repo.add_specialization(spec9)
spec10 = Specialization(species8, veterian2)
spec_repo.add_specialization(spec10)
spec11 = Specialization(species9, veterian2)
spec_repo.add_specialization(spec11)

appointment1 = Appointment('check up', '12/3/2023', '5pm', '', pet1, veterian1)
appoint_repo.add_appointment(appointment1)
appointment2 = Appointment('check up', '12/3/2023', '9am', '', pet2, veterian1)
appoint_repo.add_appointment(appointment2)
appointment3 = Appointment('sergury', '19/5/2023', '11am', '', pet2, veterian1)
appoint_repo.add_appointment(appointment3)
appointment4 = Appointment('neutralize', '25/3/2023', '2pm', '', pet2, veterian1)
appoint_repo.add_appointment(appointment4)
appointment5 = Appointment('vaccination', '8/4/2023', '3am', '', pet3, veterian2)
appoint_repo.add_appointment(appointment5)
