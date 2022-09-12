import json

class UtilsParse:
    @staticmethod
    def parse_test_data_generate():
        with open(r"..\test_data\test_data_generate.json", 'r') as file:
            data = json.load(file)
            return data

    @staticmethod
    def parse_test_data():
        with open(r"..\test_data\test_data.json", 'r') as file:
            data = json.load(file)
            return data

    @staticmethod
    def parse_data_user_id_5():
        with open(r"..\test_data\test_data_5.json", 'r') as file:
            data = json.load(file)
            return data

    @staticmethod
    def parse_test_data_post_id_99():
        with open(r"..\test_data\post_id_99.json", 'r') as file:
            data = json.load(file)
            return data
