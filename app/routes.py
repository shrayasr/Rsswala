from flask import request,session,make_response
import json

from app import conf as config
from app import app
from user import User

# /     GET
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

# /feeds    GET
# Gets the list of feeds associated to the user
@app.route("/feeds/",methods=['GET','POST'])
def feeds():

    # If user isn't there in session, throw error
    if 'user' not in session:
        return "not logged in"

    # Pick up the email
    email = session['user']

    # Get the user object
    user = User(email)

    if request.method == 'GET':

        # Get the feed list
        feedList = user.get_feed_list()

        # Make a JSON repsonse and return it
        response = make_response()
        response.mimetype="application/json"
        response.data = json.dumps(feedList)
        return response

    elif request.method == 'POST':
        
        # Pick up the required details
        feedURL = request.form['feed_url']

        # If the length of the feed URL is = 0, bump them out
        if len(feedURL.strip()) == 0:
            return "Feed URL empty"
        
        # Subscribe the user to the feed
        feedID = user.subscribe_to_feed(feedURL)
        
        # Create a response object
        responseObj = {
                "feed_id":feedID
                }

        # Make a JSON repsonse and return it
        response = make_response()
        response.mimetype="application/json"
        response.data = json.dumps(responseObj)
        return response



# /items    GET
# Get the items for all users feeds
@app.route("/feeds/items/")
def allItems():

    # If user isn't there in session, throw error
    if 'user' not in session:
        return "not logged in"

    # Pick up the user
    email = session['user']

    # Get the user object
    user = User(email)

    # Get the list of all items
    allItemsList = user.get_all_items()

    # Make a JSON response and return it
    response = make_response()
    response.mimetype="application/json"
    response.data = json.dumps(allItemsList)
    return response

# /items/<feed id>  GET
# Get the items for THAT feed
@app.route("/feeds/<feedId>/items/")
def feedItems(feedId):

    # If user isn't there in session, throw error
    if 'user' not in session:
        return "not logged in"

    # Pick up the email
    email = session['user']

    # Get a user object
    user = User(email)

    # Get the list of items for that feed
    feedItemsList = user.get_feed_items(feedId)

    # Make a JSON response and return it
    response = make_response()
    response.mimetype="application/json"
    response.data = json.dumps(feedItemsList)
    return response

@app.route("/feeds/items/<itemId>",methods=['POST'])
def markItemAsRead(feedId,itemId):

    # If user isn't there in session, throw error
    if 'user' not in session:
        return "not logged in"

    # Pick up the email
    email = session['user']

    # Get a user object
    user = User(email)

    # Mark that item as read
    markID = user.mark_item(itemId)

    # Assume that it has been marked to true
    markStatus = True
    if markID == -1:
        # Until told otherwise
        markStatus = False

    # Create a response object
    responseObj = {
            "mark_as_read":markStatus
            }

    # Make a JSON repsonse and return it
    response = make_response()
    response.mimetype="application/json"
    response.data = json.dumps(responseObj)
    return response
