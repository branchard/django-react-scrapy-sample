# django-react-scrapy-sample
A student project for training web crawling and Test driven development.

It made with Django and Scrapy libraries.

Start localy (for the first time)
---------------------------------
1. Clone the project.
2. Go into the projet directory : `$ cd django-react-scrapy-sample/`
3. Create a Python3 Virtualenv : `$ virtualenv -p python3 venv`
4. Activate the Virtualenv : `$ source venv/bin/activate`
5. Install all dependencies : `$ pip install -r requirements.txt`
6. Create the database : `$ python manage.py migrate`
7. Load default shops fixtures : `$ python manage.py loaddata default_shops`
8. Create an admin : `$ python manage.py createsuperuser`
9. Run a local server : `$ python manage.py runserver`
10. Open [127.0.0.1:8000](http://127.0.0.1:8000/) in your favorite browser.
