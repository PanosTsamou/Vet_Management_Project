from db.run_sql import run_sql

from modules.owner import Owner

def add_owner(owner):
    sql = "INSERT INTO owners(first_name, last_name, dob, address, tel_number, email, img) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [owner.first_name, owner.last_name, owner.dob, owner.address, owner.phone_number, owner.email, owner.img]
    owner.id = run_sql(sql, values)[0]['id']

def all_owners():
    owners = []
    sql = "SELECT * FROM owners"
    results = run_sql(sql)
    for row in results:
        owner = Owner(row['first_name'], row['last_name'], row['dob'], row['address'], row['email'],row['tel_number'], row['img'])
        owners.append(owner)
    return owners

def find_owner_by_id(id):
    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        owner = Owner(result['first_name'], result['last_name'], result['dob'], result['address'], result['email'],result['tel_number'], result['img'])
    return owner

def delete_all():
    sql = "DELETE  FROM owners"
    run_sql(sql)


def delete_by_id(id):
    sql = "DELETE  FROM owners WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update_owner(owner):
    sql = "UPDATE owners SET (first_name, last_name, dob, address, tel_number, email, img) VALUES (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [owner.first_name, owner.last_name, owner.dob, owner.address, owner.phone_number, owner.email, owner.img, owner.id]
    run_sql(sql, values)

