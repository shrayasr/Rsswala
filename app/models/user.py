import hashlib

from app import app

class User():

    def __init__(self,email,password,uid=None):
        self.uid = uid
        self.email = email
        self.password = password
        self.password = self.hash_pass()

    def __str__(self):
        return {
                "id":self.uid,
                "email":self.email,
                "password":self.password
                }

    def hash_pass(self):
        salted_password = self.password + app.secret_key
        return hashlib.sha1(salted_password).hexdigest()

