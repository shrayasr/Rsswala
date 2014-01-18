import MySQLdb

from instance import conf as config
from app import app
from app.models.user import User
from app.utils.commons import Commons

class UserDM():

    def __init__(self):

        self.db = MySQLdb.connect(user=config.MYSQL_USER,
                                  passwd=config.MYSQL_PASS, db=config.MYSQL_DB,
                                  charset='utf8')

    def create(self, user):
        try:
            salt = app.secret_key
            email = user.email
            password = Commons.hash_password(user.password,salt)

            c = self.db.cursor()
            c.execute("INSERT INTO users(email,password) VALUES(%s,%s)",(email,
                      password,))

        except Exception as e :
            print "Error while creating the user" 
            print e
            c.close()
            self.db.rollback()
            return None

        c.close()
        self.db.commit()
        return self.get(email)

    def get(self, email):
        user = None
        try:
            c = self.db.cursor()
            c.execute("SELECT * FROM USERS where email = %s",(email,))

            if c.rowcount > 0:
                row = c.fetchone()
                user = User(str(row[1]),str(row[2]),str(row[0]))
            
            c.close()
            return user

        except Exception as e:
            print "Error while picking up the user"
            print e
            c.close()
            return None

    def delete(self, email):
        try:
            c = self.db.cursor()
            c.execute("DELETE from USERS where email = %s",(email,))

            success = False

            if c.rowcount == 1:
                self.db.commit()
                success = True

            c.close()
            return success

        except Exception as e:
            print "Error while deleting the user"
            print e
            c.close()
            self.db.rollback()
            return None

    def change_password(self, email, oldpassword, newpassword):
        try:
            salt = app.secret_key
            oldpasswordHash = Commons.hash_password(oldpassword,salt)
            newpasswordHash = Commons.hash_password(newpassword,salt)

            currentUser = self.get(email)
            if currentUser.password != oldpasswordHash:
                print "Old password doesn't match"
                return False
            
            c = self.db.cursor()
            c.execute("UPDATE users SET password = %s where email = %s",
                      (newpasswordHash,email,))

            success = False

            if c.rowcount == 1:
                self.db.commit()
                success = True

            c.close()
            return success

        except Exception as e:
            print "Error while changing password for the user"
            print e
            c.close()
            self.db.rollback()
            return None

