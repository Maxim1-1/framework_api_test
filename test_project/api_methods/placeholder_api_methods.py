from test_project.project_utils.random_test_data import UtilsDATA
from framework.base.api_utils import ApiUtils
from framework.utils.parse_config_utils import Utils

CONFIG = Utils.parse_config()


class PlaceholderApiMethods:
    headers = CONFIG["content_type"]

    def is_validate_response_is_json_format(self, url):
        """checks that the response type is json"""
        request = ApiUtils().get(url=url).json()
        return isinstance(request[0], dict)

    def is_validate_status_code(self, url, expected_status_code):
        """compares the status code"""
        request = ApiUtils().get(url=url).status_code
        return request == expected_status_code

    def get_object_by_id(self, url):
        """returns the request object, for example post or user"""
        response_object = ApiUtils().get(url=url).json()
        return response_object

    def is_validate_post_body_empty(self, url):
        """checks that the response body is empty"""
        body = ApiUtils().get(url=url).json()
        return len(body) <= 0

    def create_new_post(self, url, generate_user_id=None, data=None):
        """creates a new post with random data and returns a response in json format"""
        UtilsDATA().write_random_test_date(generate_user_id)
        return ApiUtils().post(url=url, headers=self.headers, json=data)

    def get_user_data(self, url, number_user):
        """returns user data in json format by its id"""
        request_user_5 = ApiUtils().get(url=url).json()[number_user - 1]
        return request_user_5
