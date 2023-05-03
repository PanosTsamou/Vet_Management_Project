from flask import render_template, redirect, request
from flask import Blueprint
from modules.vet import Veterian

import repositories.veterian_repository as vet_repo
import repositories.pet_repository as pet_repo
import repositories.care_repository as care_repo

vets_blueprint = Blueprint("vets", __name__)

@vets_blueprint.route('/vets')
def all_vets():
    return render_template('mvp/vets/vets.jinja', display_vets = vet_repo.all_vets())

@vets_blueprint.route('/vets/<id>')
def veterian_info(id):
    return render_template('mvp/vets/veterian.jinja', veterian = vet_repo.find_veterian_by_id(int(id)), list_of_pets = care_repo.find_pets_by_vet(int(id)))

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
    return redirect('/vets')

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