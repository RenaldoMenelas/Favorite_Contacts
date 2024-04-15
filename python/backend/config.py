from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


#initialize Flask app

app = Flask(__name__)

#WRAP OUR APPLICATION AROUND CORS SO WE CAN MAKE REQUEST FROM DIFERENT SERVER TO OUR FLASK
CORS(app)

#setting the location of the database we will be stroing
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#instance of databse python class can modify sql
db = SQLAlchemy(app)


