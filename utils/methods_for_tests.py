import requests
from utils.http_method import Http_methods
import random
import string

"""методы для теста"""

base_url = "https://reqres.in"


class ApiMethods():
    """Метод получение id пользователя"""

    @staticmethod
    def get_sigle_user(user_id):
        get_sigle_user_resourse = f"/api/users/{user_id}"
        get_sigle_user_url = base_url + get_sigle_user_resourse
        get_sigle_user_result = Http_methods.get(get_sigle_user_url)
        return get_sigle_user_result

    """Метод для создания пользователя"""

    @staticmethod
    def create_user(name, job):
        json_create_user = {
            "name": name,
            "job": job
        }
        create_user_resourse = "/api/users"
        create_user_url = base_url + create_user_resourse
        create_user_result = Http_methods.post(create_user_url, json_create_user)
        check_post = create_user_result.json()
        user_id = check_post.get("id")
        return create_user_result

    """Метод для обновления пользователя"""

    @staticmethod
    def update_user(user_id, name, job):
        json_update_user = {
            "name": name,
            "job": job
        }
        update_user_resourse = f"/api/users/{user_id}"
        update_user_url = base_url + update_user_resourse
        update_user_result = Http_methods.put(update_user_url, json_update_user)
        return update_user_result

    """Метод для удаления пользователя"""

    @staticmethod
    def delete_user(user_id):
        delete_user_resourse = f"/api/users/{user_id}"
        delete_user_url = base_url + delete_user_resourse
        delete_user_result = Http_methods.delete(delete_user_url)
        return delete_user_result

    """Метод для получение списка пользователей"""

    @staticmethod
    def get_list_users(page):
        get_list_users_resourse = f"/api/users?page={page}"
        get_list_users_url = base_url + get_list_users_resourse
        get_list_users_result = Http_methods.get(get_list_users_url)
        return get_list_users_result

    """Метод для регистрации пользователя"""

    @staticmethod
    def reg_user(email, password):
        json_reg_user = {
            "email": email,
            "password": password
        }
        reg_user_resourses = "/api/register"
        reg_user_url = base_url + reg_user_resourses
        reg_user_result = Http_methods.post(reg_user_url, json_reg_user)
        return reg_user_result

    """Метод для входа на сайте"""

    @staticmethod
    def login(email, password):
        json_login = {
            "email": email,
            "password": password
        }

        login_resourse = "/api/login"
        login_url = base_url + login_resourse
        login_result = Http_methods.post(login_url, json_login)
        return login_result

    """Метод для теста на время ответа от сервера"""
    @staticmethod
    def get_delayed_response(delay):
        get_delayed_response_resourse = f"/api/users?delay={delay}"
        get_delayed_response_url = base_url + get_delayed_response_resourse
        get_delayed_response_result = Http_methods.get(get_delayed_response_url)
        return get_delayed_response_result

    """Метод получение списка пользователей"""
    @staticmethod
    def get_user_list(page_id):
        get_list_resourse = f"/api/users?page={page_id}"
        get_list_url = base_url + get_list_resourse
        get_list_url_result = Http_methods.get(get_list_url)
        return get_list_url_result

