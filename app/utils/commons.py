import hashlib

class Commons():

    @staticmethod
    def hash_password(password, salt):
        print password
        salted_password = password + salt
        return hashlib.sha1(salted_password).hexdigest()
