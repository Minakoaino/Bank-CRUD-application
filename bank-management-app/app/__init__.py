from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database connection URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://@localhost/BankDB?driver=ODBC+Driver+17+for+SQL+Server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the database object
db = SQLAlchemy(app)

# Import the routes and models
from app import routes, models


