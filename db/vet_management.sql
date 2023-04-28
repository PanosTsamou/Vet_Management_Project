DROP TABLE IF EXISTS vets;
DROP TABLE IF EXISTS owners;
DROP TABLE IF EXISTS animals;


CREATE TABLE owners(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    dob VARCHAR(255)
    adress VARCHAR(255),
    tel_number VARCHAR(255),
    email VARCHAR(255)
);

CREATE TABLE pets(
    id SERIAL PRIMARY KEY,
    pet_name VARCHAR(255),
    age INIT,
    pet_weight INIT
    owner_id INIT NOT NULL REFERENCES owner(id)
);

CREATE TABLE vets(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    dob VARCHAR(255)
    adress VARCHAR(255),
    tel_number VARCHAR(255),
    email VARCHAR(255)
)
