from flask import Flask
from app import conf as config

app = Flask(__name__)
app.secret_key=config.SECRET_KEY

from app import routes
