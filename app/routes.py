from flask import request,session

from app import conf as config
from app import app
from user import User

@app.route("/")
def hello():
    return "Welcome to rsswala"

@app.route("/login/", methods=['POST'])
def login():
    email = request.form['email']
    print email
    if len(email.strip()) == 0:
        return "Need email"

    # Only we can use it
    if email.upper() not in [ users.upper() for users in config.USERS ]:
        return "Private beta only"

    user = User(email)
    session['user'] = email
    return "logged in"

@app.route("/whoami/")
def whoami():
    if 'user' not in session:
        return "not logged in"
    return session['user']

@app.route("/logout/",methods=['POST'])
def logout():
    if 'user' not in session:
        return "not logged in"

    email = session['user']

    session.clear()
    return "logged out "+email
