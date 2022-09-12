from test_project.api_methods.post import Post
from framework.utils.parse_config_utils import Utils
from test_project.project_utils.utils_for_parse import UtilsParse
from test_project.api_methods.placeholder_api_methods import PlaceholderApiMethods
from test_project.constants.constants import Endpoints


CONFIG = Utils.parse_config()

DATA_FOR_NEW_POST = UtilsParse.parse_test_data_generate()
DATA_FOR_USER_ID_99 = UtilsParse.parse_test_data_post_id_99()


class PostMethods:
    url_posts = CONFIG["url"] + Endpoints.GET_ALL_POSTS

    api_methods = PlaceholderApiMethods()

    def __get_url_post_by_id(self, id_post):
        return CONFIG["url"] + Endpoints().GET_POST_BY_ID.format(id_post=id_post)

    def is_validate_status_code_all_posts(self, expected_status_code=200):
        return self.api_methods.is_validate_status_code(url=self.url_posts, expected_status_code=expected_status_code)

    def is_validate_status_code_post_id_99(self, expected_status_code=200):
        return self.api_methods.is_validate_status_code(url=self.__get_url_post_by_id(99),
                                                        expected_status_code=expected_status_code)

    def is_validate_status_code_post_id_150(self, expected_status_code=404):
        return self.api_methods.is_validate_status_code(url=self.__get_url_post_by_id(150),
                                                        expected_status_code=expected_status_code)

    def is_validate_status_code_new_post(self, expected_status_code=201):
        return self.api_methods.create_new_post(url=self.url_posts,
                                                generate_user_id=1).status_code == expected_status_code

    def is_validate_response_is_json(self, url=url_posts):
        return self.api_methods.is_validate_response_is_json_format(url=url)

    def is_validate_info_post__with_id_99(self, id_post=99):
        response = self.api_methods.get_object_by_id(self.__get_url_post_by_id(id_post))
        response_post = Post(data=response)
        expected_post = Post(data=DATA_FOR_USER_ID_99)
        return response_post == expected_post

    def is_validate_post_body_empty_by_id(self, id=None):
        return self.api_methods.is_validate_post_body_empty(url=self.__get_url_post_by_id(id))

    def is_validate_data_new_post(self):
        response = self.api_methods.create_new_post(url=self.url_posts, generate_user_id=1,
                                                    data=DATA_FOR_NEW_POST).json()
        response_post = Post(data=response)
        expected_post = Post(data=DATA_FOR_NEW_POST)
        return (response_post.userId == expected_post.userId) and (response_post.title == expected_post.title) and (
                response_post.body == expected_post.body)
