from app import app

@app.route("/")
def hello():
    return "Welcome to rsswala"
