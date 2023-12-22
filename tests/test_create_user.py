import pytest
from utils.methods_for_tests import ApiMethods
from utils.Checking import *
from test_data.json import *


class TestCreateUser():
    """Данный тест проверяет набор тестов на создание, обновление и удаление пользователя"""

    def setup_method(self):
        self.user_id = None

    """Создание пользовате"""

    def test_create_user(self):
        post_result = ApiMethods.create_user("Maria", "Boss")
        json_post_result = post_result.json()
        user_id = json_post_result.get("id")
        Checking.check_response_schema(json_post_result, schema_create_user)

    """обновление пользователя"""

    def test_update_user(self):
        put_result = ApiMethods.update_user(self.user_id, "Sasha", "customer")
        json_put_result = put_result.json()
        Checking.check_status_code(200, put_result.status_code)
        Checking.check_response_schema(json_put_result, schema_update_user)

    """Удалени пользователя"""

    def test_delete_user(self):
        delete_result = ApiMethods.delete_user(self.user_id)
        Checking.check_status_code(204, delete_result.status_code)

    """Проверка что пользователь удалён после теста"""

    def test_single_user(self):
        single_user = ApiMethods.get_sigle_user(self.user_id)
        Checking.check_status_code(404, single_user.status_code)
        assert not single_user.json()
