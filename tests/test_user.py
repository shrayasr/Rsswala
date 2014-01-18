from app.data_mappers.userDM import UserDM
from app.models.user import User

def test_create_new_user():
    email = "test@test.com"
    password = "test1234"

    user = User(email, password)
    userDM = UserDM()
    result = userDM.create(user)

    if result:
        assert True
    else:
        assert False

def test_get_user():
    email = "test@test.com"
    
    userDM = UserDM()
    user = userDM.get(email)

    if user:
        assert True
    else:
        assert False

def test_modify_user_password():
    email = "test@test.com"
    oldpassword = "test1234"
    newpassword = "touching1234"

    userDM = UserDM()
    result = userDM.change_password(email,oldpassword,newpassword)

    if result == True:
        assert True
    else:
        assert False

def test_delete_user():
    email = "test@test.com"

    userDM = UserDM()
    result = userDM.delete(email)

    if result == True:
        assert True
    else:
        assert False

