import os.path
from .neosintez_gateway import NeosintezGateway


class GetToken:

    @staticmethod
    def execute(url, auth_string):
        if os.path.isfile('test_data/token.txt'):
            with open('test_data/token.txt') as file:
                token = file.read()
        else:
            token = NeosintezGateway.get_token(url, auth_string)
        return token
