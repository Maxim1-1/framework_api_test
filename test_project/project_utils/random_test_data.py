import json
import random
import string


class UtilsDATA:

    @staticmethod
    def random_generate_data(id=None):
        lower_alphabet = list(string.ascii_lowercase)
        title = ''
        body = ''
        for i in range(7):
            title += lower_alphabet[random.randint(0, len(lower_alphabet) - 1)]
            body += lower_alphabet[random.randint(0, len(lower_alphabet) - 1)]

        data = {
            "userId": id,
            "title": title,
            "body": body
        }
        return data

    @staticmethod
    def write_random_test_date(id_user=None):
        data = json.dumps(UtilsDATA().random_generate_data(id_user))
        with open(r"..\test_data\test_data_generate.json", 'w') as file:
            file.write(data)

