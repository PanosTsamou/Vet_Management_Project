from modules.owner import Owner
from modules.vet import Veterian
from modules.pet import Pet

import repositories.owner_repository as owner_repo
import repositories.veterian_repository as vet_repo
import repositories.pet_repository as pet_repo

pet_repo.delete_all()
vet_repo.delete_all()
owner_repo.delete_all()

owner1 = Owner("Dave", "Bard", "12/3/2000", "23 Long street", "daveb@gmail.com", "77236767398", "/img/dave")
owner_repo.add_owner(owner1)
owner2 = Owner("Molly", "Brown", "20/6/2003", "23  Walnut street", "mollyb@gmail.com", "77236734658", "/img/molly")
owner_repo.add_owner(owner2)
veterian1 = Veterian("Aaron", "McCurdy", "2/7/1983", "3  Walnut street", "aaronmc@gmail.com", "77232437169", "/img/aaron")
vet_repo.add_veterian(veterian1)
veterian2 = Veterian("Patric", "Coile", "15/10/1995", "20 Mary Crescent", "patickc@gmail.com", "77232384933", "/img/patric")
vet_repo.add_veterian(veterian2)

pet1= Pet("blacky","12/3/2022",15,"male","dog")
pet1.add_owner(owner1)
pet1.add_veterian(veterian1)
pet_repo.add_pet(pet1)
pet2= Pet("fatty","12/3/2022",60,"male","dog")
pet2.add_owner(owner1)
pet2.add_veterian(veterian1)
pet_repo.add_pet(pet2)
pet3= Pet("flafy","12/3/2022",3,"male","rabbit")
pet3.add_owner(owner2)
pet3.add_veterian(veterian2)
pet_repo.add_pet(pet3)
pet4= Pet("margaret","12/3/2022",3,"female","cat")
pet4.add_owner(owner2)
pet4.add_veterian(veterian1)
pet_repo.add_pet(pet4)

