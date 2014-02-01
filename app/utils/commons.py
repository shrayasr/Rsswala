import bcrypt

class Commons():

    @staticmethod
    def hash_password(password):
        print password
        return bcrypt.hashpw(password,bcrypt.gensalt())

    @staticmethod
    def verify_password(raw_password, hashed_password):
        return hashed_password == bcrypt.hashpw(raw_password, hashed_password)
