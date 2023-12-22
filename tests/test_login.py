import pytest
import requests

from utils.methods_for_tests import ApiMethods
from utils.Checking import *


class TestPositiveLogin():
    """Тут будут позитивные тесты на логин"""

    def test_login_with_valid_date(self):
        """Тест на логин с валидными данными"""
        login_result = ApiMethods.login("eve.holt@reqres.in", "cityslicka")
        responce_json = login_result.json()
        value_token = responce_json.get("token")
        assert value_token == "QpwL5tke4Pnpja7X4", f"token value is {value_token}"

        """Тест на логин с большими буквами в емейле"""
    def test_login_with_lower(self):
        login_result = ApiMethods.login("Eve.holt@reqres.in", "cityslicka")
        responce_json = login_result.json()
        value_token = responce_json.get("token")
        assert value_token == "QpwL5tke4Pnpja7X4", f"token value is {value_token}"

        """Тест на логин с большими буквами в домене"""
    def test_login_with_higher_in_domain(self):
        login_result = ApiMethods.login("Eve.holt@Reqres.in", "cityslicka")
        responce_json = login_result.json()
        value_token = responce_json.get("token")
        assert value_token == "QpwL5tke4Pnpja7X4", f"token value is {value_token}"


class TestNegativelogin():
    """Тест на логин с некорректным емейлом"""
    def test_login_incorrect_email(self):
        login_result = ApiMethods.login("holt@Reqres.in", "cityslicka")
        Checking.check_json_value(login_result, 'error', 'user not found')

        """Тест на логин с некорректным паролем"""
    def test_login_incorrect_password(self):
        login_result = ApiMethods.login("Eve.holt@Reqres.in", "tyslicka")
        Checking.check_json_value(login_result, 'error', 'user not found')

        """Тест на логин без ввода данных"""
    def test_login_without_date(self):
        login_result = ApiMethods.login("", "")
        Checking.check_json_value(login_result, 'error', 'Missing email or username')

    """Тест на логин  ввода только емейла"""
    def test_login_with_only_emeil(self):
        login_result = ApiMethods.login("eve.holt@reqres.in", "")
        Checking.check_json_value(login_result, 'error', 'Missing password')

        """Тест на логин  ввода только пароля"""
    def test_login_with_only_password(self):
        login_result = ApiMethods.login("", "eve.holt@reqres.in")
        Checking.check_json_value(login_result, 'error', 'Missing email or username')