from test_project.project_utils.models_utils import create_attr_model_post


class Post:
    userId: int
    id: int
    title: str
    body: str

    def __init__(self, data: dict):
        create_attr_model_post(data=data, obj=self)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __getitem__(self, key):
        return self.__dict__[key]
