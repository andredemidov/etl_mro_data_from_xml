import json
from datetime import datetime
import requests


class NeosintezGateway:

    equipment_class_id = ''
    tech_position_class_id = ''
    object_repair_group_class_id = '9e8f1a26-778d-e811-810f-edf0bf5e0091'
    operation_object_class_id = 'ac65f34b-5623-ed11-9141-005056b6948b'

    toir_id_attribute_id = '73e3c201-5527-e811-810c-9ec54093bb77'
    config_attribute_id = '723bba30-4175-ed11-9152-005056b6948b'
    level_attribute_id = 'ef7b693e-46c0-ea11-9110-005056b6948b'
    parent_attribute_id = 'a607d6ef-575b-ed11-914d-005056b6948b'
    name_attribute_id = '3b1ed651-5527-e811-810c-9ec54093bb77'
    tech_number_attribute_id = 'ca97a0b1-0a29-e811-810d-c4afdb1aea70'
    toir_url_attribute_id = 'a5072ee5-f164-e811-810f-edf0bf5e0091'
    operation_date_attribute_id = '02964d6c-0b29-e811-810d-c4afdb1aea70'
    departament_id_attribute_id = '057708a1-0b29-e811-810d-c4afdb1aea70'
    object_type_attribute_id = '456b1f0f-0b29-e811-810d-c4afdb1aea70'
    operating_attribute_id = ''
    registration_number_attribute_id = 'f535c056-0b29-e811-810d-c4afdb1aea70'
    commodity_producer_attribute_id = '626cd129-e330-e811-810f-edf0bf5e0091'
    commodity_number_attribute_id = '706297c6-0a29-e811-810d-c4afdb1aea70'
    category_attribute_id = '2daf9add-0a29-e811-810d-c4afdb1aea70'

    def __init__(self, url, token):
        self._url = url
        self._token = token

    @staticmethod
    def get_token(url, auth_string) -> str:
        """
        Метод возвращает токен для аутентификации в Неосинтез на основании данных для аутентификации
        auth_string - строка вида grant_type=password&username=???&password=??&client_id=??&client_secret=??
        """
        req_url = url + 'connect/token'
        payload = auth_string
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(req_url, data=payload, headers=headers)
        if response.status_code == 200:
            return json.loads(response.text)['access_token']
        else:
            raise Exception(f'Error connect to Neosintez for url {url}')

    @staticmethod
    def get_value(attributes: dict, attribute_id: str, attribute_type='str', get_only_id=False):
        result = attributes.get(attribute_id, None)
        if result:
            item_type = result['Type']
            if item_type == 8 and get_only_id:
                return attributes[attribute_id]['Value']['Id']
            elif item_type == 8:
                return attributes[attribute_id]['Value']['Name']
            elif item_type == 3:
                value = attributes[attribute_id]['Value']
                return datetime.strptime(value, '%Y-%m-%dT%H:%M:%S')
            elif item_type == 1:
                return round(attributes[attribute_id]['Value'], 4)
            else:
                return attributes[attribute_id]['Value']
        else:
            if attribute_type == 'int':
                return 0
            elif attribute_type == 'date':
                return None
            else:
                return ''

    def make_search_request(self, route, payload) -> requests.Response:
        """Метод выполняет поисковый запрос по условиям, переданным в payload
        запрос простой - запрашивает все результаты одним запросом.
        Возвращает объект типа requests.Response"""
        req_url = self._url + route
        payload = json.dumps(payload)
        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {self._token}',
            'Content-Type': 'application/json-patch+json',
            'X-HTTP-Method-Override': 'GET'
        }
        return requests.post(req_url, headers=headers, data=payload)

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

        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {self._token}',
            'Content-Type': 'application/json-patch+json'
        }
        response = requests.put(req_url, headers=headers, data=payload)
        if response.status_code != 200:
            print(req_url)
            print(request_body)
            print(response.text)
        return response

    def create(self, parent_id, request_body) -> requests.Response:
        req_url = self._url + f'api/objects?parent={parent_id}'
        payload = json.dumps(request_body)

        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {self._token}',
            'Content-Type': 'application/json-patch+json'
        }
        response = requests.post(req_url, headers=headers, data=payload)
        if response.status_code != 200:
            print(req_url)
            print(request_body)
            print(response.text)
        return response

    def delete_collection_item(self, host, item_id):
        req_url = self._url + f'api/objects/{host}/collections/{item_id}'

        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {self._token}',
            'Content-Type': 'application/json-patch+json'
        }
        return requests.delete(req_url, headers=headers)

    def delete_item(self, item_id):
        req_url = self._url + f'api/objects/{item_id}'

        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {self._token}',
            'Content-Type': 'application/json-patch+json'
        }
        return requests.delete(req_url, headers=headers)

    def create_collection(
            self,
            host_id,
            collection_attribute_id,
            host_class_id,
            key_attribute_id=None,
            key=None
    ) -> requests.Response:
        req_url = self._url + f'api/objects/{host_id}/collections?attributeId={collection_attribute_id}'
        payload = {
            "Id": "00000000-0000-0000-0000-000000000000",
            "Name": "forvalidation",
            "Entity": {
                "Id": host_class_id,
                "Name": "forvalidation"
            }
        }
        if key and key_attribute_id:
            payload['Attributes'] = {
                key_attribute_id: {
                    "Id": key_attribute_id,
                    "Name": "forvalidation",
                    "Type": 2,
                    "Value": key
                }
            }
        payload = json.dumps(payload)
        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {self._token}',
            'Content-Type': 'application/json-patch+json'
        }
        return requests.post(req_url, headers=headers, data=payload)

    def get_collections(self, host, collection_attribute_id) -> requests.Response:
        req_url = self._url + f'api/objects/{host}/collections?attributeId={collection_attribute_id}&Take=100'

        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {self._token}',
            'Content-Type': 'application/json-patch+json'
        }
        return requests.get(req_url, headers=headers)
