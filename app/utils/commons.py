import bcrypt

class Commons():

    @staticmethod
    def hash_password(password, salt):
        print password
        return bcrypt.hashpw(password,bcrypt.gensalt())

    @staticmethod
    def verify_password(raw_password, hashed_password):
        return hashed_password == bcrypt(raw_password, hashed_password)
