# Vet_Management_Project

hello!!!

To run this app you should have installed python, flask and sql.

If you have those already you can run the app.

Before running the app there are 3 steps you have to do. In your terminal, at  app's path, run those commands:

1) Create a database:
    > createdb vet

2) Create tables:
    > psql -d vet -f db/vet_management.sql

3)Populate the database:
    > python3 populate.py


NOW YOU ARE READY TO RUN THE APP

RUN THE APP:
    > flask run

RUN TESTS:
    > python3 run_test.py

