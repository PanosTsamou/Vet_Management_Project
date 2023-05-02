DROP TABLE IF EXISTS appointments;
DROP TABLE IF EXISTS specializations;
DROP TABLE IF EXISTS owners_users;
DROP TABLE IF EXISTS vets_users;
DROP TABLE IF EXISTS admins;
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

CREATE TABLE owners_users(
    id SERIAL PRIMARY KEY,
    user_name VARCHAR(255),
    password VARCHAR(255),
    owner_id INT NOT NULL REFERENCES owners(id)
);
CREATE TABLE vets_users(
    id SERIAL PRIMARY KEY,
    user_name VARCHAR(255),
    password VARCHAR(255),
    vet_id INT NOT NULL REFERENCES vets(id)
);
CREATE TABLE admins(
    id SERIAL PRIMARY KEY,
    user_name VARCHAR(255),
    password VARCHAR(255)
);

CREATE TABLE pets(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob VARCHAR(255),
    weight INT,
    sex VARCHAR(255),
    species VARCHAR(255),
    breed VARCHAR(255),
    img VARCHAR(255), 
    treatment  VARCHAR(255),
    chipped BOOLEAN,
    chip_number VARCHAR(255),
    -- species_id INT NOT NULL REFERENCES species(id),
    -- breed_id INT NOT NULL REFERENCES breeds(id),
    owner_id INT NOT NULL REFERENCES owners(id),
    veterian_id INT NOT NULL REFERENCES vets(id)
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




