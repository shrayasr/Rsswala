from flask import request,session

from app import conf as config
from app import app
from user import User

# Welcome them to rsswala
@app.route("/")
def hello():
    return "Welcome to rsswala"

# /login     POST
# Logs the person into rsswala
# Currently it is in private beta so only some emails are allowed
@app.route("/login/", methods=['POST'])
def login():

    # If the user already has logged in, return
    if 'user' in session:
        return session['user'] + " is already logged in"

    # Pick up the email
    email = request.form['email']

    # If the email is empty, throw them out
    if len(email.strip()) == 0:
        return "Need email"

    # Only we can use it
    if email.upper() not in [ users.upper() for users in config.USERS ]:
        return "Private beta only"

    # Create the user object
    user = User(email)

    # Store the email in session
    session['user'] = email
    return "logged in"

# /whoami   GET
# Tells you who you are (email id)
@app.route("/whoami/")
def whoami():

    # if the user isn't there in sesion, throw error
    if 'user' not in session:
        return "not logged in"

    # else, return an error
    return session['user']

# /logout   POST
# Logs out the currently logged in user
@app.route("/logout/",methods=['POST'])
def logout():

    # If user isn't there in session, throw error
    if 'user' not in session:
        return "not logged in"

    # Pick up the email
    email = session['user']

    # clear the session
    session.clear()

    return "logged out "+email
