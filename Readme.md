## Weather CRUD test app

# Requirements:
`Python 3.6.1`
`Postgresql`

# Installation

1. Clone project.
`https://github.com/djangodev1231/weatherproject`

2. Install all dependencies with virtualenv

   cd weatherproject

   virtualenv venv

   source venv/bin/activate

   pip3 install -r requirements.txt

3. Allow our user to create test db in the postgresql console:

   ALTER USER weather CREATEDB;

4. Run unit test

   python manage.py test

5. Run Integration test

   Test by postman using the collection inside RestAPI/tests
