from flask import render_template, redirect, request
from flask import Blueprint
from modules.vet import Veterian
from modules.specialization import Specialization

import repositories.specialization_repository as spec_repo
import repositories.species_repository as species_repo
import repositories.veterian_repository as vet_repo
import repositories.pet_repository as pet_repo
import repositories.care_repository as care_repo

vets_blueprint = Blueprint("vets", __name__)

@vets_blueprint.route('/vets')
def all_vets():
    return render_template('mvp/vets/vets.jinja', display_vets = vet_repo.all_vets())

@vets_blueprint.route('/vets/<id>')
def veterian_info(id):
    return render_template('mvp/vets/veterian.jinja', veterian = vet_repo.find_veterian_by_id(int(id)), list_of_pets = care_repo.find_pets_by_vet(int(id)), specializations = spec_repo.find_species_by_vet(int(id)))

@vets_blueprint.route('/vets/<id>/delete', methods= ["POST"])
def delete_veterian(id):
    vet_repo.delete_by_id(int(id))
    return redirect('/vets')

@vets_blueprint.route('/vets/<id>/edit', methods = ["POST"])
def edit_veterian_details(id):
    return render_template('mvp/vets/veterian_edit.jinja', veterian = vet_repo.find_veterian_by_id(int(id)))

@vets_blueprint.route('/vets/<id>', methods = ["POST"] )
def update_veterian_details(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    dob = request.form['dob']
    address = request.form['address']
    phone_number = request.form['phone_number']
    email = request.form['email']
    veterian = Veterian(first_name, last_name, dob, address, email, phone_number)
    veterian.add_id(id)
    vet_repo.update_vets(veterian)
    return redirect(f'/vets/{veterian.id}')

@vets_blueprint.route("/vets/new-veterian")
def new_veterian_form():
    return render_template("mvp/vets/new_veterian.jinja")

@vets_blueprint.route("/vets", methods=["POST"])
def create_veterian():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    dob = request.form['dob']
    address = request.form['address']
    phone_number = request.form['phone_number']
    email = request.form['email']
    veterian = Veterian(first_name, last_name, dob, address, email, phone_number)
    vet_repo.add_veterian(veterian)
    return redirect('/vets')

@vets_blueprint.route("/vets/<id>/specialization/edit")
def edit_spec(id):
    return render_template("/mvp/vets/specialization_edit.jinja", veterian = vet_repo.find_veterian_by_id(int(id)), specializations = spec_repo.find_species_by_vet(int(id)), species = species_repo.all_species())

@vets_blueprint.route("/vets/<id>/specialization/edit", methods=["POST"])
def change_spec(id):
    specialization_species = species_repo.find_species_by_id(request.form['specialization'])
    species = species_repo.find_species_by_id(request.form['species'])
    veterian = vet_repo.find_veterian_by_id(int(id))
    specialization = spec_repo.find_specialization_by_species_and_veterian_id(specialization_species.id, veterian.id)
    new_specialization = Specialization(species, veterian, specialization.id)
    spec_repo.update(new_specialization)
    return redirect(f'/vets/{veterian.id}')

@vets_blueprint.route("/vets/<id>/specialization/new")
def new_spec(id):
    list_of_species= []
    species = species_repo.all_species()
    specializations = spec_repo.find_species_by_vet(int(id))
    for spec in species[::-1]:
        for special in specializations:
            if  spec.__eq__(special):
                species.remove(spec)

    return render_template("/mvp/vets/specialization_add.jinja", veterian = vet_repo.find_veterian_by_id(int(id)), species = species)

@vets_blueprint.route("/vets/<id>/specialization/new", methods=["POST"])
def add_spec(id):
    species = species_repo.find_species_by_id(request.form['species'])
    veterian = vet_repo.find_veterian_by_id(int(id))
    specialization = Specialization(species, veterian)
    spec_repo.add_specialization(specialization)
    return redirect(f'/vets/{veterian.id}')

@vets_blueprint.route("/vets/<id>/specialization/delete")
def delete_spec(id):
    return render_template("/mvp/vets/specialization_delete.jinja", veterian = vet_repo.find_veterian_by_id(int(id)), specializations = spec_repo.find_species_by_vet(int(id)))

@vets_blueprint.route("/vets/<id>/specialization/delete", methods=["POST"])
def remove_spec(id):

    specialization = spec_repo.find_specialization_by_species_and_veterian_id(request.form['specialization'], int(id))
    spec_repo.delete_by_id(specialization.id)
    return redirect(f'/vets/{id}')