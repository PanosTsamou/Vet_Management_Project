from flask import render_template, redirect, request
from flask import Blueprint
from modules.pet import Pet
import repositories.pet_repository as pet_repo
import repositories.owner_repository as owner_repo
import repositories.veterian_repository as vet_repo


pets_blueprint = Blueprint("pets", __name__)

@pets_blueprint.route('/pets')
def all_pets():
    all_pets_to_display = pet_repo.all_pets()
    print("pets!!!", all_pets_to_display)
    return render_template("mvp/pets/pets.jinja", all_pets_to_display = all_pets_to_display)

@pets_blueprint.route('/pets/<id>/delete',  methods = ["POST"])
def delete_pet(id):
    pet_repo.delete_by_id(int(id))
    return redirect('/pets')
    
@pets_blueprint.route("/pets/<id>")
def pet_display(id):
    pet= pet_repo.find_pet_by_id(int(id))
    return render_template("mvp/pets/pet.jinja", pet = pet)

@pets_blueprint.route("/pets/<id>/edit", methods=["POST"])
def delete_edit(id):
    return render_template("/mvp/pets/pet_edit.jinja", pet = pet_repo.find_pet_by_id(int(id)), vets = vet_repo.all_vets(), owners = owner_repo.all_owners())

@pets_blueprint.route("/pets/<id>", methods=["POST"])
def pet_edit(id):
    name = request.form['name']
    dob = request.form['dob']
    species = request.form['species']
    sex = request.form['sex']
    weight = int(request.form['weight'])
    chipped = request.form['chipped']
    veterian = vet_repo.find_veterian_by_id(request.form['veterian'])
    owner = owner_repo.find_owner_by_id(request.form['owner'])
    pet = Pet(name,dob,weight,sex,species)
    pet.add_veterian(veterian)
    pet.add_owner(owner)
    pet.add_id(id)
    if chipped == "True":
        pet.change_chip_status()
    pet_repo.update_pets(pet)
    return redirect('/pets')

@pets_blueprint.route('/pets/new-pet')
def new_pet_form():
    return render_template('/mvp/pets/new_pet.jinja', vets = vet_repo.all_vets(), owners = owner_repo.all_owners())

@pets_blueprint.route('/pets', methods=["POST"])
def add_new_pet():
    name = request.form['name']
    dob = request.form['dob']
    species = request.form['species']
    sex = request.form['sex']
    weight = int(request.form['weight'])
    chipped = request.form['chipped']
    veterian = vet_repo.find_veterian_by_id(request.form['veterian'])
    owner = owner_repo.find_owner_by_id(request.form['owner'])
    pet = Pet(name,dob,weight,sex,species)
    pet.add_veterian(veterian)
    pet.add_owner(owner)
    pet_repo.add_pet(pet)
    if chipped == "True":
        pet.change_chip_status()
    pet_repo.update_pets(pet)
    return redirect("/pets")

