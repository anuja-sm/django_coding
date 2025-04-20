# django_coding
# SWAPI. Django coding

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv {env_name}
$ source {env_name}/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd swapi_project
(env)$ python3 manage.py runserver
```
And navigate to `http://localhost:8000/`.


## Database Migration

To run the server, `cd` into the directory where `manage.py` is:

Run the migrations
```sh
(env)$ python3 manage.py makemigrations
(env)$ python3 manage.py migrate
```

