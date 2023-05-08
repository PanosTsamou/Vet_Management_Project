from  db.run_sql import run_sql
from modules.species import Species

def add_species(species):
    sql = "INSERT INTO species(name) VALUES (%s) RETURNING * "
    values = [species.name]
    species.id = run_sql(sql,values)[0]['id']

def all_species():
    species_to_desplay = []
    sql = "SELECT * FROM species"
    results = run_sql(sql)
    for row in results: 
        species = Species(row['name'], row['id'])
        species_to_desplay.append(species)
    return species_to_desplay

def find_species_by_id(id):
    sql = "SELECT * FROM species WHERE id= %s"
    values=[id]
    result = run_sql(sql,values)
    if result:
        result = result[0]
        species = Species(result['name'], result['id'] )
        
    return species

def delete_all():
    sql = "DELETE  FROM species"
    run_sql(sql)


def delete_by_id(id):
    sql = "DELETE  FROM species WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update_species(species):
    sql = "UPDATE species SET (name) = (%s) WHERE id = %s"
    values = [species.name, species.id]
    run_sql(sql, values)