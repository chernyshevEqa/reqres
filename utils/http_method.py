import requests
import allure

from utils.Logger import Logger

class Http_methods():
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    cookies = ''

    """метод get"""

    @staticmethod
    def get(url):
        with allure.step("put"):
            Logger.add_request(url, method='GET')
            result = requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookies)
            Logger.add_response(result)
            return result

    """метод post"""

    @staticmethod
    def post(url, body):
        with allure.step("post"):
            Logger.add_request(url, method='POST')
            result = requests.post(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookies)
            Logger.add_response(result)
            return result

    """метод put"""

    @staticmethod
    def put(url, body):
        with allure.step("put"):
            Logger.add_request(url, method="PUT")
            result = requests.put(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookies)
            Logger.add_response(result)
            return result

    """метод delete"""
    @staticmethod
    def delete(url):
        with allure.step("delete"):
            Logger.add_request(url, method="DELETE")
            result = requests.delete(url, headers=Http_methods.headers, cookies=Http_methods.cookies)
            Logger.add_response(result)
            return result

