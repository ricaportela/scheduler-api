Getting Started
---------------

### Initial Setup ###
1. Make a new virtualenv: ``virtualenv .venv``
2. Activate the virtualenv: ``source .venv/bin/activate``
3. Install Django: ``pip install -r requirements.txt``
4. Edit ``feira/settings.py:108`` to match your LANGUAGE_CODE 
5. Run the server: ``python app.py``

Solution
-------------------
Development an API with Flask

To acess API thru Browser
------------------------------
* List of Schedules
 ``http://127.0.0.1:8000/schedules`` 

* Detail Schedule
 ``http://127.0.0.1:8000/schedules/1/``
