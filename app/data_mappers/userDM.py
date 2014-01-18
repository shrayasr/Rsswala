import MySQLdb

from instance import conf as config
from app.models.user import User

class UserDM():

    def __init__(self):

        self.db = MySQLdb.connect(user=config.MYSQL_USER,
                                  passwd=config.MYSQL_PASS, db=config.MYSQL_DB,
                                  charset='utf8')

    def create_user(self, user):
        try:
            email = user.email
            password = user.password

            c = self.db.cursor()
            c.execute("INSERT INTO users(mail,password) VALUES(%s,%s)",(email,
                      password,))

        except Exception as e :
            print "Error while creating the user" 
            print e
            self.db.rollback()
            return None

        self.db.commit()
        return c.lastrowid
