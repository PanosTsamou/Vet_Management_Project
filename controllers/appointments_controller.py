from flask import render_template, redirect, request, url_for
from flask import Blueprint
from modules.pet import Pet
from modules.care import Care
from modules.species import Species
from modules.appointment import Appointment

import repositories.appointment_repository as appoint_repo
import repositories.species_repository as species_repo
import repositories.specialization_repository as spec_repo
import repositories.pet_repository as pet_repo
import repositories.owner_repository as owner_repo
import repositories.veterian_repository as vet_repo
import repositories.care_repository as care_repo


appointments_blueprint = Blueprint("appointment", __name__)

@appointments_blueprint.route('/appointments')
def all_appointments():
    all_appointments_to_display = appoint_repo.all_appointments()

    return render_template("/mvp/appointments/appointments.jinja", all_appointments_to_display = all_appointments_to_display, vets = vet_repo.all_vets())

@appointments_blueprint.route('/appointments/<id>/delete',  methods = ["POST"])
def delete_appointment(id):
    
    appoint_repo.delete_by_id(int(id))
    if 'owner_page' in request.form:
        return  redirect( url_for('owners.owner_info', id= request.form['owner_page']))
    elif 'veterian_page' in request.form:
        return  redirect( url_for('vets.veterian_info', id= request.form['iveterian_page']))
    else:
        return redirect('/appointments')
    
@appointments_blueprint.route("/appointments/<id>")
def appointment_display(id):
    appointment = appoint_repo.find_appointment_by_id(int(id))
    return render_template("mvp/appointments/appointment.jinja", appointment = appointment)

@appointments_blueprint.route("/appointments/<id>/edit", methods=["POST"])
def delete_edit(id):
    appointment = appoint_repo.find_appointment_by_id(int(id))
    vets = spec_repo.find_vet_by_species_id(appointment.pet.species.id)
    print("!!!!!!!!!!!!!!!", vets)
    return render_template("/mvp/appointments/edit_appointment.jinja", appointment = appointment, vets = vets)

@appointments_blueprint.route("/appointments/<id>", methods=["POST"])
def pet_edit(id):
    name = request.form['name']
    dob = request.form['dob']
    species = species_repo.find_species_by_id(request.form['species'])
    breed = request.form['breed']
    sex = request.form['sex']
    weight = int(request.form['weight'])
    chipped = request.form['chipped']
    treatment = request.form['treatment']
    veterian = vet_repo.find_veterian_by_id(request.form['veterian'])
    owner = owner_repo.find_owner_by_id(request.form['owner'])
    pet = Pet(name,dob,weight,sex,species,breed, treatment)
    pet.add_owner(owner)
    pet.add_id(int(id))
    if chipped == "True":
        pet.change_chip_status()
    pet_repo.update_pets(pet)
    care = care_repo.find_care_by_pet_id(int(id))
    if care == None:
        care = Care(pet,veterian)
        care_repo.add_care(care)
    else:
        care = Care(pet,veterian,care.id)
        care_repo.update(care)
    return redirect(f'/pets/{pet.id}')

@appointments_blueprint.route('/appointments/new-appointment')
def new_appointment_form():
    return render_template('/mvp/appointments/new_appointment.jinja', vets = vet_repo.all_vets(),pets = pet_repo.all_pets())

@appointments_blueprint.route('/appointments', methods=["POST"])
def add_new_appointment():
    title = request.form['title']
    date = request.form['date']
    time = request.form['time']
    description = request.form['description']
    veterian = vet_repo.find_veterian_by_id(request.form['veterian'])
    pet = pet_repo.find_pet_by_id(request.form['pets'])
    appointment = Appointment(title, date, time, description, pet, veterian)
    appoint_repo.add_appointment(appointment)
    return redirect("/appointments")

