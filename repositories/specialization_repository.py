from db.run_sql import run_sql

from modules.specialization import Specialization
from modules.species import Species
from modules.vet import Veterian

import repositories.species_repository as species_repo
import repositories.pet_repository as pet_repo
import repositories.veterian_repository as vet_repo
import repositories.owner_repository as owner_repo

def add_specialization(specialization):
     sql = "INSERT INTO specializations ( species_id, veterian_id ) VALUES ( %s, %s) RETURNING id"
     values = [specialization.species.id, specialization.veterian.id]
     specialization.id = run_sql(sql, values)

def all_specializations():
    all_specializations = []
    sql = "SELECT * FROM specializations"
    results = run_sql(sql)
    for row in results:
        species = species_repo.find_species_by_id(row['species_id'])
        veterian = vet_repo.find_veterian_by_id(row['veterian_id'])
        specialization = Specialization(species, veterian, row['id'])
        all_specializations.append(specialization)
    return all_specializations

def find_specialization_by_id(id):
    specialization = None
    sql = "SELECT * FROM specializations WHERE id= %s"
    values = [id]
    result = run_sql(sql, values)
    if result:
        result = result[0]
        species = species_repo.find_species_by_id(result['species_id'])
        veterian = vet_repo.find_veterian_by_id(result['veterian_id'])
        specialization = Specialization(species, veterian, result['id'])
    return specialization



def find_species_by_vet(veterian_id):
    species = []
    sql = "SELECT species.* FROM species INNER JOIN specializations ON specializations.species_id = species.id WHERE veterian_id = %s"
    values = [veterian_id]
    results = run_sql(sql, values)
    for row in results:
        a_species = Species(row['name'], row['id']) 
        species.append(a_species)
    return species

def find_vet_by_species_id(species_id):
    veterians = []
    sql = "SELECT vets.* FROM vets INNER JOIN specializations ON specializations.veterian_id = vets.id WHERE species_id = %s"
    values = [species_id]
    result = run_sql(sql, values)
    if result:
        result = result[0]
        veterian = Veterian(result['first_name'], result['last_name'], result['dob'], result['address'], result['email'], result['tel_number'])
        veterian.add_id(result['id'])
        veterians.append(veterian)
    return veterians

def find_specialization_by_species_and_veterian_id(species_id, veterian_id):
    specialization = None
    sql = "SELECT * FROM specializations  WHERE species_id = %s AND veterian_id = %s"
    values = [species_id, veterian_id]
    result = run_sql(sql, values)
    if result:
        result = result[0]
        species = species_repo.find_species_by_id(result['species_id'])
        veterian = vet_repo.find_veterian_by_id(result['veterian_id'])
        specialization = Specialization(species, veterian, result['id'])
    return specialization

def delete_all():
    sql = "DELETE FROM specializations"
    run_sql(sql)

def delete_by_id(id):
    sql = "DELETE FROM specializations WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(specialization):
    sql = "UPDATE specializations SET (species_id, veterian_id ) = ( %s, %s) WHERE id = %s"
    values = [specialization.species.id, specialization.veterian.id, specialization.id]
    run_sql(sql, values)
