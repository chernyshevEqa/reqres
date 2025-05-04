from faker import Faker
import pytest


"""Фикстура для генерации пароля"""
@pytest.fixture
def generate_upper_password():
    faker = Faker("ru_RU")
    password = faker.password()
    return password.upper()

"""Фикстура для генерации емейла и пароля"""
@pytest.fixture
def generate_test_data():
    faker = Faker("ru_RU")
    email = faker.email()
    password = faker.password()
    return email, password

"""Фикстура для генерации емейла c цифрами"""
@pytest.fixture
def generate_email_with_ascii():
    faker = Faker()
    email_with_symbols = faker.email()
    random_numbers = faker.random_number(digits=3)
    full_email = f"{random_numbers}{email_with_symbols}"
    print("ok")
    return full_email