from db.run_sql import run_sql

from modules.pet import *
from modules.owner  import Owner
from modules.vet import Veterian

import repositories.veterian_repository as vet_repo
import repositories.owner_repository as owner_repo


def add_pet(pet):
    sql = "INSERT INTO pets(name, dob, weight, sex, species, breed, img, treatment, chipped, chip_number,  owner_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,  %s, %s, %s) RETURNING * "
    values = [pet.name, pet.dob, pet.weight, pet.sex, pet.species, pet.breed, pet.img, pet.treatment, pet.chipped, pet.chip_number,pet.owner.id]
    pet.id = run_sql(sql,values)[0]['id']

def all_pets():
    pets = []
    sql = "SELECT * FROM pets"
    results = run_sql(sql)
    for row in results:
        owner= owner_repo.find_owner_by_id(row['owner_id'])
        pet = Pet(row['name'], row['dob'], row['weight'], row['sex'], row['species'], row['breed'], row['img'], row['treatment'], row['chipped'], row['chip_number'], owner, row['id'] )
        pets.append(pet)
    return pets

def find_pet_by_id(id):
    sql = "SELECT * FROM pets WHERE id= %s"
    values=[id]
    result = run_sql(sql,values)[0]
    if result:
        owner= owner_repo.find_owner_by_id(result['owner_id'])
        pet = Pet(result['name'], result['dob'], result['weight'], result['sex'], result['species'], result['breed'], result['treatment'], result['img'], result['chipped'], result['chip_number'], owner, result['id'] )
        
    return pet

def find_pet_by_owner_id(owner_id):
    pets = []
    sql = "SELECT * FROM pets WHERE owner_id= %s"
    values=[owner_id]
    results = run_sql(sql,values)
    for row in results:
        owner= owner_repo.find_owner_by_id(row['owner_id'])
        pet = Pet(row['name'], row['dob'], row['weight'], row['sex'], row['species'], row['breed'], row['img'], row['treatment'], row['chipped'], row['chip_number'], owner, row['id'] )
        pets.append(pet)
    return pets
# def find_owner_by_pet_id(pet_id):
#     pets = []
#     sql = "SELECT * FROM pets WHERE veterian_id= %s"
#     values=[veterian_id]
#     results = run_sql(sql,values)
#     for row in results:
#         owner= owner_repo.find_owner_by_id(row['owner_id'])
#         veterian =  vet_repo.find_veterian_by_id(row['veterian_id'])
#         pet = Pet(row['name'], row['dob'], row['weight'], row['sex'], row['species'], row['breed'], row['img'], row['treatment'], row['chipped'], row['chip_number'], owner, veterian, row['id'] )
#         pets.append(pet)
#     return pets

def delete_all():
    sql = "DELETE  FROM pets"
    run_sql(sql)


def delete_by_id(id):
    sql = "DELETE  FROM pets WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update_pets(pet):
    sql = "UPDATE pets SET (name, dob, weight, sex, species, breed, img, treatment, chipped, chip_number,  owner_id) = (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [pet.name, pet.dob, pet.weight, pet.sex, pet.species, pet.breed, pet.img, pet.treatment, pet.chipped, pet.chip_number,pet.owner.id, pet.id]
    run_sql(sql, values)

