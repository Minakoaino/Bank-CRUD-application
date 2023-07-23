import flask
from flask import Flask
app = Flask(__name__)

# Import the Flask app instance
from app import app

if __name__ == '__main__':
    app.run(debug=True)