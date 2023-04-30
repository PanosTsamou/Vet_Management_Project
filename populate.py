from modules.owner import Owner
from modules.vet import Veterian

import repositories.owner_repository as owner_repo
import repositories.veterian_repository as vet_repo


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