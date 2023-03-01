import os.path
from .neosintez_gateway import NeosintezGateway


class GetToken(NeosintezGateway):

    def __init__(self, url):
        token = ''
        super().__init__(url, token)

    def execute(self, auth_string):
        if os.path.isfile('test_data/token.txt'):
            with open('test_data/token.txt') as file:
                token = file.read()
        else:
            token = self.get_token(self._url, auth_string)
        return token
