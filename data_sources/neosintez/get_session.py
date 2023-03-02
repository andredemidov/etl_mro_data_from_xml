import os.path
from requests import Session
from .neosintez_gateway import NeosintezGateway


class GetSession:

    @staticmethod
    def execute(url, auth_string):
        session = Session()

        if os.path.isfile('test_data/token.txt'):
            with open('test_data/token.txt') as file:
                token = file.read()
        else:
            token = NeosintezGateway.get_token(url, auth_string, session)

        session.headers.update(
            {
                'Accept': 'application/json',
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json-patch+json'
            }
        )
        return session
