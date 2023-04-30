from db.run_sql import run_sql

from modules.vet import Veterian

def add_veterian(veterian):
    sql = "INSERT INTO vets(first_name, last_name, dob, address, tel_number, email, img) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [veterian.first_name, veterian.last_name, veterian.dob, veterian.address, veterian.phone_number, veterian.email, veterian.img]
    veterian.id = run_sql(sql, values)[0]['id']

def all_owners():
    vets = []
    sql = "SELECT * FROM vets"
    results = run_sql(sql)
    for row in results:
        owner = Veterian(row['first_name'], row['last_name'], row['dob'], row['address'], row['email'],row['tel_number'], row['img'])
        vets.append(owner)
    return vets

def find_owner_by_id(id):
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        owner = Veterian(result['first_name'], result['last_name'], result['dob'], result['address'], result['email'],result['tel_number'], result['img'])
    return owner

def delete_all():
    sql = "DELETE  FROM vets"
    run_sql(sql)


def delete_by_id(id):
    sql = "DELETE  FROM vets WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update_owner(veterian):
    sql = "UPDATE vets SET (first_name, last_name, dob, address, tel_number, email, img) VALUES (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [veterian.first_name, veterian.last_name, veterian.dob, veterian.address, veterian.phone_number, veterian.email, veterian.img, veterian.id]
    run_sql(sql, values)

