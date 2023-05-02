from flask import render_template, redirect, request
from flask import Blueprint
from modules.owner import Owner

import repositories.owner_repository as owner_repo
import repositories.pet_repository as pet_repo

owners_blueprint = Blueprint("owners", __name__)

@owners_blueprint.route('/owners')
def all_owners():
    return render_template('mvp/owners/owners.jinja', display_owners = owner_repo.all_owners())

@owners_blueprint.route('/owners/<id>')
def owner_info(id):
    return render_template('mvp/owners/owner.jinja', owner = owner_repo.find_owner_by_id(int(id)), list_of_pets = pet_repo.find_pet_by_owner_id(int(id)))

@owners_blueprint.route('/owners/<id>/delete', methods= ["POST"])
def delete_owner(id):
    owner_repo.delete_by_id(id)
    return redirect('/owners')

@owners_blueprint.route('/owners/<id>/edit', methods = ["POST"])
def edit_owner_details(id):
    return render_template('mvp/owners/owner_edit.jinja', owner = owner_repo.find_owner_by_id(int(id)))

@owners_blueprint.route('/owners/<id>', methods = ["POST"] )
def update_owner_details(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    dob = request.form['dob']
    address = request.form['address']
    phone_number = request.form['phone_number']
    email = request.form['email']
    owner = Owner(first_name, last_name, dob, address, email, phone_number)
    owner.add_id(id)
    owner_repo.update_owner(owner)
    return redirect('/owners')