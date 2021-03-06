[![Build Status](https://travis-ci.org/branchard/django-react-scrapy-sample.svg?branch=master)](https://travis-ci.org/branchard/django-react-scrapy-sample)
[![Dependency Status](https://www.versioneye.com/user/projects/587eb137b194d40038f4727b/badge.svg?style=flat)](https://www.versioneye.com/user/projects/587eb137b194d40038f4727b)
[![Code Climate](https://codeclimate.com/github/branchard/django-react-scrapy-sample/badges/gpa.svg)](https://codeclimate.com/github/branchard/django-react-scrapy-sample)

# django-react-scrapy-sample
A student project for training web crawling and Test driven development.

It made with Django and Scrapy libraries.

System dependencies (not exhaustive)
------------------------------------
- python3.4/3.5 (3.6 is not supported because scrapy-djangoitem do not support this specific version)
- python-virtualenv
- python-pip
- nodejs

Start localy (for the first time)
---------------------------------
1. Clone the project.
2. Go into the projet directory : `$ cd django-react-scrapy-sample/`
3. Create a Python3 Virtualenv : `$ virtualenv -p python3.5 venv`
4. Activate the Virtualenv : `$ source venv/bin/activate`
5. Install all python dependencies (this step can be long) : `$ pip install -r requirements.txt`
6. Init the nodeenv : `$ nodeenv -p`
7. Install all node dependencies : `$ npm install`
8. Create the database : `$ python manage.py migrate`
9. Load default shops fixtures : `$ python manage.py loaddata default_shops`
10. Load sample items : `$ python manage.py loaddata sample_items`
11. Create an admin : `$ python manage.py createsuperuser`
12. Scrap sample items : `scrapy crawl shopscraper`
13. Run a local server : `$ python manage.py runserver`
14. Open [127.0.0.1:8000](http://127.0.0.1:8000/) in your favorite browser.
