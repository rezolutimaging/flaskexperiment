from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__) 

#set configuration variable to connect to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://udacitystudios:udacityrocks!@localhost:5432/example'  

#initialize sqlalchemy database 
db = SQLAlchemy(app)

#create a person model 
class Person(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

#create database tables 
db.create_all()


@app.route('/')
def index():
	person = Person.query.first()
	return 'Hello ' + person.name

