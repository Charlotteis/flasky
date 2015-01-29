27/01/2015
----------
- set up repo
- pip3 install flask
- Basic hello world application

- pip3 install flask-script
- Use Manager to run app with command-line arguments
- Created templates folder and base, index and user templates.
- Set view logic to only render templates, separating business and presentation logic

- pip3 install flask-bootstrap
- import bootstrap into app
- implement pretty bootstrap user template
- Make all templates inherit from base, which inherits from bootstrap base
- Simply all non-base templates
- Add 404 and 500 templates

- pip3 install flask-moment (moment.js)
- import flask-moment into app
- display UTC time converted into local time in index template

- pip3 install flask-wtf
- add really basic secret key to enable CSRF protection for flask-wtf to work
- import flask-wtf form and wtform fields and validators into app
- create a basic form and include it in index.html
- render form in index view
- Implement redirects and user sessions to avoid form resubmission
- flashed messages (?)

- pip3 install flask-sqlalchemy
- import sqlalchemy into app & set database
- Write database models
- Add dummy data to db
- Add db to .gitignore
- work with database in index view
- add database imports to shell using manager command

- pip3 install flask-migrate
- import migrate into app
- add manager command for db migration
- initialise a migration folder -> python3 app.py db init
- create a migration script -> python3 app.py db migrate -m "message"
- upgrade database -> python3 app.py db upgrade

- pip3 install flask-mail
- configure app to send email through gmail account
- uninstall flask-mail as not working

- Begin restructuring application
- create config.py file
- create app folder, move templates and static into it
- create app/main
- create app/main/__init__.py
- create blueprint for routes and error page handlers
- restructure app into multiple files and folders

29/01/2914
----------
- set up basic test files
- add test command to manage.py (move manage to right place)

- add password hashing to user model
- add user model password tests

- create auth folder with views and templates
- pip3 install flask-login (user authentication)
- update user model with the flask-login user mixin
- add email field to user model
- initialise flask-login
- create login form
