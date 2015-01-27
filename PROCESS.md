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

- pip install flask-moment (moment.js)
- import flask-moment into app
- display UTC time converted into local time in index template

- pip install flask-wtf
- add really basic secret key to enable CSRF protection for flask-wtf to work
- import flask-wtf form and wtform fields and validators into app
- create a basic form and include it in index.html
