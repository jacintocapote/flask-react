# Bank Admin Dashboard Example with Flask.

How execute this example:

1.- First enable virtualenv for python.
   1.- cd /api
   2.- python3 -m venv .
   3.- source ./bin/active
   4.- Execute flask --app api db upgrade
   4.- Then from root application execute: npm run dev


This command will launch react and flask server using forward from port 3000/api to flask.

For execute tests:
   1.- Inside api folder execute: 
       pytest test_flask_api.py
   2.- We have folder in the root documentation with folder with swager and postman tests.
