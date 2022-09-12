from framework.base.api_utils import ApiUtils
from test_project.api_methods.posts_methods import PostMethods


class Steps:

    def is_check_posts_sort(self):
        all_id = [i['id'] for i in ApiUtils().get(url=PostMethods.url_posts).json()]
        for i in all_id:
            if i >= i + 1:
                return False
            return True
