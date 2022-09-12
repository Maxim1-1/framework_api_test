from test_project.project_utils.models_utils import create_attr_model_user


class User:
    def __init__(self, data: dict):
        create_attr_model_user(data=data, obj=self)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
