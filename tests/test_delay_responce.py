import pytest
import requests
from utils.methods_for_tests import ApiMethods
from utils.Checking import *

class TestDelayResponce():

    """Тест проверки времени ответа от сервера"""
    def test_delay_responce(self):
        url = "https://reqres.in/api/users?delay=3"
        Checking.test_api_response_time(url)

    def test_negative_delay(self):
        delay_result = ApiMethods.get_delayed_response(-1)






