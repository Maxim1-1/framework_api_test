import pytest
from ..steps.steps import Steps
from ..api_methods.posts_methods import PostMethods
from ..api_methods.users_methods import UsersMethods


class Test:

    post = PostMethods()
    user = UsersMethods()

    def test_get_all_posts(self):
        assert self.post.is_validate_status_code_all_posts(), f"Ошибка статут кода, статус код={self.post.is_validate_status_code_all_posts()}"
        assert self.post.is_validate_response_is_json(), "Возвращаемый тип данных не json формата"
        assert Steps().is_check_posts_sort(), "Значение списка json не отсоритрованы по id"

    def test_get_99_post(self):
        assert self.post.is_validate_status_code_post_id_99(), f"Ошибка статут кода, статус код={self.post.is_validate_status_code_post_id_99()}"
        assert self.post.is_validate_info_post__with_id_99(), 'Информация в ответе от сервера некоректна'

    @pytest.mark.parametrize("id_post", [150])
    def test_status_code_404(self, id_post):
        assert self.post.is_validate_status_code_post_id_150(), f"Ошибка статут кода, статус код={self.post.is_validate_status_code_post_id_150()}"
        assert self.post.is_validate_post_body_empty_by_id(id_post), "Тело запроса для id 150 не пусто"

    def test_create_post(self):
        assert self.post.is_validate_status_code_new_post(), f"Ошибка статут кода, статус код={self.post.is_validate_status_code_new_post()}"
        assert self.post.is_validate_data_new_post(), "Данные запросы и ответа не совпадают"

    def test_get_users(self):
        assert self.user.is_validate_status_code_all_users(),f"Ошибка статут кода, статус код={self.user.is_validate_status_code_all_users()}"
        assert self.user.is_validate_response_is_json(), "Возвращаемый тип данных не json формата"
        assert self.user.is_validate_user_5_in_all_users(), "Данные User№5 не совпадают с ожидаемыми"

    def test_get_user_5(self):
        assert self.user.is_validate_status_code_user_id_5(), f"Ошибка статут кода, статус код={self.user.is_validate_status_code_user_id_5()}"
        assert self.user.is_validate_data_user_id_5(), "Данные User№5 не совпадают с ожидаемыми"
