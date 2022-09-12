from framework.utils.parse_config_utils import Utils
from test_project.api_methods.placeholder_api_methods import PlaceholderApiMethods
from test_project.constants.constants import Endpoints
from test_project.api_methods.user import User
from test_project.project_utils.utils_for_parse import UtilsParse

CONFIG = Utils.parse_config()
DATA_USER_5 = UtilsParse.parse_data_user_id_5()


class UsersMethods:
    url_users = CONFIG["url"] + Endpoints.GET_ALL_USERS

    api_methods = PlaceholderApiMethods()

    def __get_url_user_by_id(self, id_user=None):
        return CONFIG["url"] + Endpoints().GET_USER_BY_ID.format(id_user=id_user)

    def is_validate_status_code_all_users(self, expected_status_code=200):
        return self.api_methods.is_validate_status_code(url=self.url_users, expected_status_code=expected_status_code)

    def is_validate_status_code_user_id_5(self, expected_status_code=200):
        return self.api_methods.is_validate_status_code(url=self.__get_url_user_by_id(5),
                                                        expected_status_code=expected_status_code)

    def is_validate_response_is_json(self, url=url_users):
        return self.api_methods.is_validate_response_is_json_format(url=url)

    def is_validate_post_body_empty_by_id(self):
        return self.api_methods.is_validate_post_body_empty(url=self.url_users)

    def get_user_5_in_all_users(self, number_user=5):
        response_user_id_5 = self.api_methods.get_user_data(url=self.url_users, number_user=number_user)
        user_5 = User(response_user_id_5)
        return user_5

    def is_validate_user_5_in_all_users(self):
        user = self.get_user_5_in_all_users()
        expected_user_data = User(data=DATA_USER_5)
        return user == expected_user_data

    def is_validate_data_user_id_5(self):
        response = self.api_methods.get_object_by_id(url=self.__get_url_user_by_id(5))
        user = self.get_user_5_in_all_users()
        expected_user_data = User(data=response)
        return user == expected_user_data
