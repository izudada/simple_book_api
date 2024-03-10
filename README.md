##  A simple Book API


## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/izudada/downtime_monitor.git
```

Create a virtual environment to install dependencies and activate it use the link below first to install virtualenv [here](https://help.dreamhost.com/hc/en-us/articles/115000695551-Installing-and-using-virtualenv-with-Python-3#:~:text=Virtualenv%20is%20a%20tool%20used,the%20globally%20installed%20libraries%20either).)

After installation create a virtual environment by running:

```sh
$ virtualen env_name
```

Next, activate the virtual enviroment with :

```sh
$ source env_name/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```


Use migrate command to effect database model:

```sh
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
```

Start the server with:
```sh
$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`


##  Documentation

Postman documentation can be found [Here](https://documenter.getpostman.com/view/20677030/2s8ZDR7kSF)

### Import Postman Collection
You can import the postman collection "Inventory Management System.postman_collection.json"
to test the endpoints locally. by importing Web "Monitor.postman_collection.json" into postman

Note: Postman collection also contain tests for each endpoint

##  Test

To run all available tests use:

```sh
$ python manage.py test
```

### Useful resources

- [Django Crontab](https://pypi.org/project/django-crontab/)




coverage run manage.py test && coverage report && coverage html