# Bank Admin Dashboard Example with Flask.

How execute this example:

First enable virtualenv for python.
   * cd /api
   * python3 -m venv .
   * source ./bin/active
   * Execute flask --app api db upgrade
   * Then from root application execute: npm run dev


This command will launch react and flask server using forward from port 3000/api to flask.

For execute tests:
   * Inside api folder execute: 
       pytest test_flask_api.py
   * We have folder in the root documentation with folder with swager and postman tests.
