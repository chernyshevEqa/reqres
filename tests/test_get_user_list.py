import random
from test_data.json import *
from utils.methods_for_tests import ApiMethods
from utils.Checking import *
class TestPositiveGetListUser():

    """Метод получение списка пользователей"""
    def test_get_user_list(self):
        random_number = Checking.create_random_number()
        get_user_list_result = ApiMethods.get_user_list(random_number) #ввод номера страницы
        Checking.check_status_code(get_user_list_result.status_code, 200)
        Checking.check_json_value(get_user_list_result, "page", random_number)
        Checking.check_response_schema(get_user_list_result.json(), schema_get_user_list)
        Checking.check_headers(get_user_list_result)

class TestNegativeGetListUser():
    random_number = Checking.create_random_number()

    """получение списка несуществующей странице"""
    def test_get_user_list_invalid_page(self):
        get_user_list_result = ApiMethods.get_user_list(13)
        Checking.check_status_code(get_user_list_result, 200)


