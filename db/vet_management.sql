DROP TABLE IF EXISTS appointments;
DROP TABLE IF EXISTS specializations;

DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS breeds;
DROP TABLE IF EXISTS vets;
DROP TABLE IF EXISTS species;
DROP TABLE IF EXISTS owners;


CREATE TABLE owners(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    dob VARCHAR(255),
    address VARCHAR(255),
    tel_number VARCHAR(255),
    email VARCHAR(255),
    img VARCHAR(255)
);

CREATE TABLE species(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE breeds(
    id SERIAL PRIMARY KEY,
    breed VARCHAR(255)
);

CREATE TABLE vets(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    dob VARCHAR(255),
    address VARCHAR(255),
    tel_number VARCHAR(255),
    email VARCHAR(255),
    img VARCHAR(255)
);

CREATE TABLE pets(
    id SERIAL PRIMARY KEY,
    pet_name VARCHAR(255),
    dob VARCHAR(255),
    pet_weight INT,
    owner_id INT NOT NULL REFERENCES owners(id),
    species_id INT NOT NULL REFERENCES species(id),
    breed_id INT NOT NULL REFERENCES breeds(id),
    chipped BOOLEAN,
    chip_number INT,
    sex VARCHAR(255),
    pet_img VARCHAR(255)
);



CREATE TABLE appointments(
    id SERIAL PRIMARY KEY,
    pet_id INT NOT NULL REFERENCES pets(id),
    vets_id INT NOT NULL REFERENCES vets(id),
    description VARCHAR(255)
);


CREATE TABLE specializations(
    id SERIAL PRIMARY KEY,
    species_id INT NOT NULL REFERENCES species(id),
    vets_id INT NOT NULL REFERENCES vets(id)
);




