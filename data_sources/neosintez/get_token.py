from .neosintez_gateway import NeosintezGateway


class GetToken(NeosintezGateway):

    def __init__(self, url):
        token = ''
        super().__init__(url, token)

    def execute(self, auth_string):
        return self.get_token(self._url, auth_string)
