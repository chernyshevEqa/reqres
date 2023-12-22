import datetime
import os



class Logger():
    log_directory = os.path.abspath('D:\\python\\test_project\\logs\\')

    @classmethod
    def ensure_directory_exists(cls):
        if not os.path.exists(cls.log_directory):
            os.makedirs(cls.log_directory)

    @classmethod
    def write_log(cls, data: str):
        file_name = 'D:\\python\\test_project\\logs\\' + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"
        with open(file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_request(cls, url: str, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_add = f"\n------\n"
        data_add += f"Test: {test_name}\n"
        data_add += f"Time: {str(datetime.datetime.now())}\n"
        data_add += f"Request method: {method}\n"
        data_add += f"Request url: {url}\n"
        data_add += "\n"

        cls.write_log(data_add)


    @classmethod
    def add_response(cls, result):
        cookies_as_dict = dict(result.cookies)
        headers_as_dict = dict(result.headers)
        data_add = f"Response code: {result.status_code}\n"
        data_add += f"Response text: {result.text}\n"
        data_add += f"Response headers: {headers_as_dict}"
        data_add += f"Response cookies: {cookies_as_dict}"
        data_add += "\n"

        cls.write_log(data_add)

#
#
#
#
