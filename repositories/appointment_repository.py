from db.run_sql import run_sql

from modules.appointment import Appointment
from modules.pet import Pet
from modules.vet import Veterian

import repositories.species_repository as species_repo
import repositories.pet_repository as pet_repo
import repositories.veterian_repository as vet_repo
import repositories.owner_repository as owner_repo


def add_appointment(appointment):
     sql = "INSERT INTO appointments (title, date, time, description, pet_id, veterian_id ) VALUES ( %s, %s, %s, %s, %s,%s) RETURNING id"
     values = [appointment.title, appointment.date, appointment.time, appointment.description, appointment.pet.id, appointment.veterian.id]
     appointment.id = run_sql(sql, values)

def all_appointments():
    all_appointments = []
    sql = "SELECT * FROM appointments"
    results = run_sql(sql)
    for row in results:
        pet = pet_repo.find_pet_by_id(row['pet_id'])
        veterian = vet_repo.find_veterian_by_id(row['veterian_id'])
        appointment = Appointment(row['title'], row['date'], row['time'], row['description'],pet, veterian, row['id'])
        all_appointments.append(appointment)
    return all_appointments

def find_appointment_by_id(id):
    appointment = None
    sql = "SELECT * FROM appointments WHERE id= %s"
    values = [id]
    result = run_sql(sql, values)
    if result:
        result = result[0]
        pet = pet_repo.find_pet_by_id(result['pet_id'])
        veterian = vet_repo.find_veterian_by_id(result['veterian_id'])
        appointment = Appointment(result['title'], result['date'], result['time'], result['description'],pet, veterian, result['id'])
    return appointment

def find_appointments_by_pet_id(id):
    appointments = []
    sql = "SELECT * FROM appointments WHERE pet_id= %s"
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        pet = pet_repo.find_pet_by_id(row['pet_id'])
        veterian = vet_repo.find_veterian_by_id(row['veterian_id'])
        appointment = Appointment(row['title'], row['date'], row['time'], row['description'],pet, veterian, row['id'])
        appointments.append(appointment)
    return appointments

def find_appointments_by_veterian_id(id):
    appointments = []
    sql = "SELECT * FROM appointments WHERE veterian_id= %s"
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        pet = pet_repo.find_pet_by_id(row['pet_id'])
        veterian = vet_repo.find_veterian_by_id(row['veterian_id'])
        appointment = Appointment(row['title'], row['date'], row['time'], row['description'],pet, veterian, row['id'])
        appointments.append(appointment)
    return appointments

def delete_all():
    sql = "DELETE FROM appointments"
    run_sql(sql)

def delete_by_id(id):
    sql = "DELETE FROM appointments WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(appointment):
    sql = "UPDATE appointments SET (title, date, time, description, pet_id, veterian_id ) = ( %s, %s, %s, %s, %s,%s) WHERE id = %s"
    values = [appointment.title, appointment.date, appointment.time, appointment.description, appointment.pet.id, appointment.veterian.id, appointment.id]
    run_sql(sql, values)

