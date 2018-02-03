Getting Started
---------------

### Initial Setup ###
1. Make a new virtualenv: ``virtualenv .venv``
2. Activate the virtualenv: ``source .venv/bin/activate``
3. Install: ``pip install -r requirements.txt``
4. Run the server: ``python run.py``

Solution
-------------------
Development an API with Flask

To access API thru Browser
------------------------------
* List of Appointments
 ``http://127.0.0.1:5000/appointments`` 

* Detail Appointments
 ``http://127.0.0.1:5000/appointments/1/``


To access API on Heroku
------------------------------
* List all appointements
``https://scheduler-desafio-api.herokuapp.com/appointments``

* Get an appointement
``https://scheduler-desafio-api.herokuapp.com/appointment/1``
