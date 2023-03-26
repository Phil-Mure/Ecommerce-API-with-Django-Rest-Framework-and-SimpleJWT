# E-commerce with Django Rest Framework (DRF) 

The code in this repo gives a simple blueprint (boilerplate) for creating an ecommerce application with Django Restfull API's using Django's Simple JWT for authentication over the API


## Project Summary

To have the read/write access via the DRF Browsable API, you'll have to be Signed in or you'll just have read-only access. Therefore, createsuperuser and then create users from the admin or via the API. To access pages, below are root urls:

```
http://127.0.0.1:8000/api/, http://127.0.0.1:8000/api/users/, http://127.0.0.1:8000/admin/
```

To authenticate via API, kindly follow the link below to learn more about DRF SimpleJWT:

```
https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html 
```

You can get tokens to pass in your requests using the the following url:

```
http://127.0.0.1:8000/api/token/
```

---

## Running this project

To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pip install virtualenv
```

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

```
virtualenv env
```

That will create a new folder `env` in your project directory. Next activate it with this command on mac/linux:

```
source env/bin/active 
```

```
env/Scripts/active (on windows)
```

Then install the project dependencies with

```
pip install -r requirements.txt
```

```
python manage.py migrate
```

```
python manage.py makemigrations user 
```

```
python manage.py migrate user
```

```
python manage.py makemigrations api 
```

```
python manage.py migrate api
```

Create a super user

```
python manage.py createsuperuser
```

Now you can run the project with this command

```
python manage.py runserver
```
