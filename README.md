# The-Gram
### An instagram clone , July 20th, 2018.
#### By **[Ephantus karanja](https://github.com/ephantuskaranja)**
## Description
This application is built on python Django framework. It is an instagram clone. The app authenticates through
email, a user can follow, like another user and see posted pictures.

##Prerequisites
  -Ubuntu Software
  -Python3.6
  -Postgres
  -python virtualenv

## Technologies Used
    1. Python 3.6
    2. HTML
    3. Bootstrap 4
    4. JavaScript
    5. Heroku
    6. Postgresql
    7. Django

## Cloning Repository
  - Clone the Repo from here [https://github.com/ephantuskaranja/Epha-gram.git]

## Create a Virtual environment
  -go to the root directory of the app, open terminal then:
  -use this command:'''virtualenv -p python3.6 virtual'''

## Install Dependencies
  * Install dependancies that will create an environment for the app to run. pip install -r requirements.txt

## Create the Database
  * psql
  * CREATE DATABASE gram;

## .env file
    SECRET_KEY = '<Secret_key>'
    DBNAME = 'gram'
    USER = '<Username>'
    PASSWORD = '<password>'
    DEBUG = True

    ensure you change this file with your database info, then

## Run migrations
  * '''python3.6 manage.py makemigrations Photomania'''
  * '''python3.6 manage.py migrate'''

## Run the App
    '''python3.6 manage.py runserver'''

## Known Bugs
    No bugs so far. If found, email me at ephantusslogan@gmail.com

## Contributions
    Incase you want to contribute, kindly feel free to clone the repo and pull request to merge.


## Support and contact details
Contact me on ephantusslogan@gmail.com for any comments, reviews or advice.

## License
Copyright (c) **Ephantus Karanja**
    MIT
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
