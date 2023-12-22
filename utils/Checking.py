import jsonschema
import pytest
import requests
import random

"""Методы для проверки ответов запросов"""
class Checking():
    """Метод для проверки статус кода"""
    @staticmethod
    def check_status_code(result, status_code):
        assert result == status_code, f"status code is {result}"

    """Метод для проверки значения в json"""
    @staticmethod
    def check_json_value(result, value, expected_result):
        value_json = result.json()
        get_value = value_json.get(value)
        assert get_value == expected_result, f"expected value is {get_value}"

    """Метод для проверки времени ответа от сервера"""
    @pytest.mark.parametrize("api_url", ["https://reqres.in/api/users?delay=1"])
    def test_api_response_time(api_url):
        response = requests.get(api_url)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        max_response_time = 4.0
        response_time = response.elapsed.total_seconds()
        assert response_time < max_response_time, f"Response time too long: {response_time} seconds"
        print(f"API response time: {response_time} seconds")

    """Метод для проверки json схемы"""
    @staticmethod
    def check_response_schema(response_json, json_schema):
        try:
            jsonschema.validate(response_json, json_schema)
            print("JSON-ответ соответствует JSON-схеме.")
            return True
        except jsonschema.exceptions.ValidationError as e:
            print(f"Ошибка валидации JSON-ответа: {e}")
            return False

    @staticmethod
    def create_random_number():
        random_number = random.randint(1, 12)
        return random_number

    """Метод для проверки заголовков"""
    @staticmethod
    def check_headers(result):
        assert 'Content-Type' in result.headers, f"{result}"
        content_type_header = result.headers.get('Content-Type')
        assert content_type_header == 'application/json; charset=utf-8', f"{content_type_header}"
