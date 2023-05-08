from db.run_sql import run_sql

from modules.care import Care
from modules.pet import Pet
from modules.vet import Veterian

import repositories.species_repository as species_repo
import repositories.pet_repository as pet_repo
import repositories.veterian_repository as vet_repo
import repositories.owner_repository as owner_repo

def add_care(care):
     sql = "INSERT INTO care ( pet_id, veterian_id ) VALUES ( %s, %s) RETURNING id"
     values = [care.pet.id, care.veterian.id]
     care.id = run_sql(sql, values)

def all_care():
    all_care = []
    sql = "SELECT * FROM care"
    results = run_sql(sql)
    for row in results:
        pet = pet_repo.find_pet_by_id(row['pet_id'])
        veterian = vet_repo.find_veterian_by_id(row['veterian_id'])
        care = Care(pet, veterian, row['id'])
        all_care.append(care)
    return all_care

def find_care_by_id(id):
    care = None
    sql = "SELECT * FROM care WHERE id= %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result:
        result = result[0]
        pet = pet_repo.find_pet_by_id(result['pet_id'])
        veterian = vet_repo.find_veterian_by_id(result['veterian_id'])
        care = Care(pet, veterian, result['id'])
    return care



def find_pets_by_vet(veterian_id):
    pets = []
    sql = "SELECT pets.* FROM pets INNER JOIN care ON care.pet_id = pets.id WHERE veterian_id = %s"
    values = [veterian_id]
    results = run_sql(sql, values)
    for row in results:
        owner= owner_repo.find_owner_by_id(row['owner_id'])
        species =    species_repo.find_species_by_id(row['species_id']) 
        pet = Pet(row['name'], row['dob'], row['weight'], row['sex'], species, row['breed'], row['img'], row['treatment'], row['chipped'], row['chip_number'], owner, row['id'] )
        pets.append(pet)
    return pets

def find_vet_by_pet_id(pet_id):
    veterian = None
    sql = "SELECT vets.* FROM vets INNER JOIN care ON care.veterian_id = vets.id WHERE pet_id = %s"
    values = [pet_id]
    result = run_sql(sql, values)
    if result:
        result = result[0]
        veterian = Veterian(result['first_name'], result['last_name'], result['dob'], result['address'], result['email'], result['tel_number'])
        veterian.add_id(result['id'])
    return veterian
def find_care_by_pet_id(pet_id):
    care = None
    sql = "SELECT * FROM care  WHERE pet_id = %s"
    values = [pet_id]
    result = run_sql(sql, values)
    if result:
        result = result[0]
        pet = pet_repo.find_pet_by_id(result['pet_id'])
        veterian = vet_repo.find_veterian_by_id(result['veterian_id'])
        care = Care(pet, veterian, result['id'])
    return care

def delete_all():
    sql = "DELETE FROM care"
    run_sql(sql)

def delete_by_id(id):
    sql = "DELETE FROM care WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(care):
    sql = "UPDATE care SET (pet_id, veterian_id ) = ( %s, %s) WHERE id = %s"
    values = [care.pet.id, care.veterian.id, care.id]
    run_sql(sql, values)
