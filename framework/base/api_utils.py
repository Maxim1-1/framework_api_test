import requests


class ApiUtils:
    @staticmethod
    def get(url):
        request = requests.get(url)
        return request

    @staticmethod
    def post(url=None, headers=None, data=None, json=None):
        request = requests.post(url=url, headers=headers, json=json, data=data)
        return request

    @staticmethod
    def delete(url=None):
        request = requests.delete(url)

    @staticmethod
    def put(url=None):
        request = requests.put(url)
