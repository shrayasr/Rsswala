from flask import Flask
from instance import conf as config

# Create an instance of flask
app = Flask(__name__)

# Set the secret key for session use
app.secret_key=config.SECRET_KEY

# Plug in the routes
from app import routes
