from app.data_mappers.userDM import UserDM
from app.models.user import User

def test_create_new_user():
    email = "test@test.com"
    password = "test1234"

    user = User(email, password)
    userDM = UserDM()
    result = userDM.create_user(user)

    if result:
        assert True
    else:
        assert False
