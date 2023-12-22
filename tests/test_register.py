import pytest
from test_data.json import *
from tests.fixtures_for_test import *
from utils.methods_for_tests import ApiMethods
from utils.Checking import *

class TestRegistePositive():
    """Тест на регистрицию"""

    @pytest.mark.skip
    def test_register(self, generate_test_data):
        email = generate_test_data
        password = generate_test_data
        register_result = ApiMethods.reg_user(email, password)
        Checking.check_response_schema(register_result.json(), schema_register)
        Checking.check_status_code(register_result.status_code, 200)

    """Тест на регистрицию используя цифры в имени почты"""

    @pytest.mark.skip
    def test_registration_with_ascii_in_mail_name(self, generate_email_with_ascii):
        full_email = generate_email_with_ascii
        register_result = ApiMethods.reg_user(full_email, "qwerty123")
        Checking.check_status_code(register_result.status_code, 200)

    """Тест на регистрицию используя ,верхний регистр в пароле"""
    @pytest.mark.skip
    def test_registration_with_upper_password(self, generate_upper_password):
        password = generate_upper_password
        registr_result = ApiMethods.reg_user("test@mail.ru", password)
        Checking.check_status_code(registr_result.status_code, 200)

class TestRegisterNegative():

    def test_register_without_data(self):
        register_result = ApiMethods.reg_user("", "")
        Checking.check_status_code(register_result.status_code, 400)
        Checking.check_json_value(register_result, "error", "Missing email or username")

    def test_register_without_email(self, generate_test_data):
        password = generate_test_data
        register_result = ApiMethods.reg_user("", password)
        Checking.check_status_code(register_result.status_code, 400)
        Checking.check_json_value(register_result, "error", "Missing email or username")

    def test_register_without_password(self, generate_test_data):
        email = generate_test_data
        register_result = ApiMethods.reg_user(email, "")
        Checking.check_status_code(register_result.status_code, 400)
        Checking.check_json_value(register_result, "error", "Missing password")

