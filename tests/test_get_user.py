from utils.methods_for_tests import ApiMethods
from utils.Checking import *

class TestPositiveGetUser():

    """Метод получение информации о пользователе"""
    def test_get_user(self):
        get_user_result = ApiMethods.get_sigle_user(3) #ввод id пользователя
        get_user_result_json = get_user_result.json()
        Checking.check_status_code(get_user_result.status_code, 200)

    """Метод получение информации по каждому пользователю"""
    def test_get_user_info(self):
        for i in range(1, 13):
            get_info_result = ApiMethods.get_sigle_user(i)
            get_id = get_info_result.json().get("data").get("id")
            assert get_id == i

class TestNegativeGetUser():

    """Метод получение информации о несуществующем пользователе"""
    def test_get_user_incorrect_user_id(self):
        get_user_result = ApiMethods.get_sigle_user(25) #ввод несуществующего id пользователя
        Checking.check_status_code(get_user_result.status_code, 404)


