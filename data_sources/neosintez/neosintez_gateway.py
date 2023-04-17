import json
import requests
import logging


class NeosintezGateway:

    def __init__(self, url, session):
        self._url = url
        self._session = session

    @staticmethod
    def get_token(url, auth_string, session: requests.Session) -> str:
        """
        Method to get OAuth2.0 token from neosintez
        :param url: url of neosintez web portal
        :param auth_string: payload for authentication as string like grant_type=password&username=???&password=??&client_id=??&client_secret=??
        :param session: session object
        :return: token
        """
        req_url = url + 'connect/token'
        payload = auth_string
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = session.post(req_url, data=payload, headers=headers)
        if response.status_code == 200:
            return json.loads(response.text)['access_token']
        else:
            raise Exception(f'Error connect to Neosintez for url {url}')

    def make_search_request(self, route, payload) -> requests.Response:
        """Метод выполняет поисковый запрос по условиям, переданным в payload
        запрос простой - запрашивает все результаты одним запросом.
        Возвращает объект типа requests.Response"""
        req_url = self._url + route
        payload = json.dumps(payload)
        headers = {
            'X-HTTP-Method-Override': 'GET'
        }
        return self._session.post(req_url, headers=headers, data=payload)

    def make_smart_search_request(self, payload) -> list:
        """Метод выполняет поисковый запрос по условиям, переданным в payload
        запрос сначала определяет количество результатов, и если это количество превышает заданный шаг,
        запрос выполняется несколько раз получая данные по частям,
        каждый раз получая количество результата равное шагу.
        Возвращает список результатов"""
        route = f'api/objects/search?take={0}&skip={0}'
        count_response = self.make_search_request(route, payload)
        total = json.loads(count_response.text)['Total']
        print(f'total {total}')
        counter = 0
        step = 10000
        result = list()

        while counter < total:
            take = total - counter if total - counter <= step else step
            route = f'api/objects/search?take={take}&skip={counter}'
            response = self.make_search_request(route, payload)
            result.extend(json.loads(response.text)['Result'])
            counter += take
        return result

    def put_attributes(self, item_id, request_body) -> requests.Response:
        req_url = self._url + f'api/objects/{item_id}/attributes'
        payload = json.dumps(request_body)

        response = self._session.put(req_url, data=payload)
        if response.status_code != 200:
            print(req_url)
            print(request_body)
            print(json.loads(response.text))
        return response

    def create_item(self, parent_id, creation_request_body, collection_attribute_id=None) -> requests.Response:
        req_url = self._url + f'api/objects?parent={parent_id}'
        if collection_attribute_id:
            req_url = self._url + f'/api/objects/{parent_id}/collections?attributeId={collection_attribute_id}'

        payload = json.dumps(creation_request_body)

        response = self._session.post(req_url, data=payload)

        if response.status_code != 200:
            print(req_url)
            print(creation_request_body)
            print(json.loads(response.text))
        return response

    def delete_item(self, item_id, host_id=None):
        req_url = self._url + f'api/objects/{item_id}'
        if host_id:
            req_url = self._url + f'api/objects/{host_id}/collections/{item_id}'

        return self._session.delete(req_url)

    def get_collections(self, host, collection_attribute_id) -> requests.Response:
        req_url = self._url + f'api/objects/{host}/collections?attributeId={collection_attribute_id}&Take=100'
        return self._session.get(req_url)

    def change_parent(self, item_id, parent_item_id):
        req_url = self._url + f'api/objects/{item_id}/parent?parentId={parent_item_id}'
        return self._session.put(req_url)

    def _get_id_by_name(self, parent_id, class_id, name):
        req_url = self._url + 'api/objects/search?take=30'
        payload = json.dumps({
            "Filters": [
                {
                    "Type": 4,
                    "Value": parent_id
                },
                {
                    "Type": 5,
                    "Value": class_id
                }
            ],
            "Conditions": [
                {
                    'Value': name,
                    'Operator': 1,
                    'Type': 2,
                }
            ]
        })
        headers = {
            'X-HTTP-Method-Override': 'GET'
        }
        response = self._session.post(req_url, headers=headers, data=payload)
        response_text = json.loads(response.text)
        if response.status_code == 200 and response_text['Total'] == 1:
            return response_text['Result'][0]['Object']['Id']
        elif response.status_code == 200 and response_text['Total'] > 1:
            logging.warning(f'More then one result is found for {parent_id}, class id {class_id}, value {name}')
            return None
        else:
            return None

    def _get_id_by_key(self, parent_id, class_id, value, attribute_value_id):
        req_url = self._url + 'api/objects/search?take=30'
        payload = json.dumps({
            "Filters": [
                {
                    "Type": 4,
                    "Value": parent_id
                },
                {
                    "Type": 5,
                    "Value": class_id
                }
            ],
            "Conditions": [
                {
                    'Value': value,
                    'Operator': 1,
                    'Type': 1,
                    'Attribute': attribute_value_id,
                }
            ]
        })
        headers = {
            'X-HTTP-Method-Override': 'GET'
        }
        response = self._session.post(req_url, headers=headers, data=payload)
        response_text = json.loads(response.text)
        if response.status_code == 200 and response_text['Total'] == 1:
            return response_text['Result'][0]['Object']['Id']
        elif response.status_code == 200 and response_text['Total'] > 1:
            logging.warning(f'More then one result is found for {parent_id}, class id {class_id}, value {value}')
            return None
        else:
            return None

    def get_host_collections(self, host_id, collection_attribute_id):
        req_url = self._url + f'api/objects/{host_id}/collections?attributeId={collection_attribute_id}&Take=1000'
        response = self._session.get(req_url)
        return response
