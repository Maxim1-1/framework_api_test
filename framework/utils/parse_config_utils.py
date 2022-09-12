import json


class Utils:
    @staticmethod
    def parse_config():
        with open(r"..\config\config.json", 'r') as file:
            config = json.load(file)
            return config

