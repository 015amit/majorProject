To run this project in your development machine, follow these steps:


(optional) Create a virtual environment to install dependencies in and activate it:

$ python -m venv venv
$ venv/Scripts/Activate

Then install the dependencies:
(venv)$ pip install -r requirements.txt

Note the (venv) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.

Once pip has finished downloading the dependencies:
(env)$ python manage.py runserver


Open your browser and go to http://127.0.0.1:8000