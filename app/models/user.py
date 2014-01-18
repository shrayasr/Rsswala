from app import app
from app.utils.commons import Commons

class User():

    def __init__(self,email,password,uid=None):
        self.uid = uid
        self.email = email
        self.password = password

    def __str__(self):
        return {
                "id":self.uid,
                "email":self.email,
                "password":self.password
                }

