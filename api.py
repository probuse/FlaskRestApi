"""
Contains all information about the API
Source: 
FlaskRestless Documentation: http://flask-restless.readthedocs.io/en/latest/
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager

# Create a Flask appllication and the Flask-SQLAlchemy object.
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/etwin.db'
db = SQLAlchemy(app)

# Create Flask-SQLAlchemy models
class Person(db.Model):
    "handles information about person object"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode)
    birth_date = db.Column(db.Date)


class Article(db.Model):
    "Controls all information about article object"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode)
    published_at = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    author = db.relationship(Person, backref=db.backref('articles', lazy='dynamic'))



# Create database tables
db.create_all()

# create a Flask-Restless API Manager
manager = APIManager(app, flask_sqlalchemy_db=db)

# create endpoints
# by default endpoints available at /api/<tablename> ie <base_url>/api/person
manager.create_api(Person, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Article, methods=['GET']) # You can specify Http methods

# start the flask loop
app.run()