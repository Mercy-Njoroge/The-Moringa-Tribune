# Awwards
#### Application to post projects to be rated by other users,August 2020 
#### By **Mercy-Njoroge**

## Description
This is an app that allows users to like post and comment on other people posts

## Features
* User can log in to application and view other peoples posts.
* A user can rate a post.
* A user can upload posts and edit their profile.
* Admin can regulate images uploaded by deleting from the admin dashboard as well as completely close a users account.

## Setup/Installation requirements
1.Clone or download and unzip the repository from github,https://github.com/Mercy-Njoroge/Awwards.git

2. Activate virtual environment using python3.6 source venv/bin/activate

3. Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt
4. Create the Database
5. Create .env file and pastethe following filling where appropriate:

-SECRET_KEY = '<Secret_key>'
-DBNAME = 'instacopy'
-USER = '<Username>'
-PASSWORD = '<password>'
-DEBUG = True
6. Run initial Migration
-python3.6 manage.py makemigrations
-python3.6 manage.py migrate
7. Run the app
-python3.6 manage.py runserver
-Open terminal on localhost:8000


 ## Testing
 with the virtual enviroment active,run  ./manage.py test


## Technologies Used
* PYTHON 3.6
* DJANGO FRAMEWORK
* BOOTSTRAP
* CSS
* POSTGRESS

## Support and contact details
contact me @ aprilkasha42@gmail.com
### License
The project is under MIT license
Copyright 2020.All rigths reserved
  