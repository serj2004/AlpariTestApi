import json
import requests
import pytest


class TestApi3:

    i = ''
    URL = f"https://dairy.intrtl.tech/api/v1/stores/?limit={i}"
    HEADERS = {"Authorization": "Bearer f983aa91-2fd2-491c-96f3-87b9b56bc95c"}
    PARAMS = {'id': 'null', 'name': "", 'address': "", 'city_id': "", 'city_name': "", 'region_id': 0, 'region_name': "",
                    'store_type_id': "", 'store_type_name': "", 'segment_id': "", 'external_id': "",
                    'external_id2': "", 'territory1_id': "", 'territory': "", 'retailer_id': "",
                    'retailer_name': "", 'lon': 0, 'lat': 0, 'category': "", 'type': "", 'active_matrices_count': 0}

    def test1(self):

        """Проверка равенства возвращаемого массива указанному лимиту"""

        i = str(15)
        res = requests.get(self.URL + i, headers=self.HEADERS)
        body = json.loads(res.content)
        assert (len(body['data'])) <= int(i)

    def test2(self):

        """Проверка возвращаемого кода"""

        res = requests.get(self.URL, headers=self.HEADERS)
        assert res.status_code == 200

    def test3(self):

        """Проверка возвращаемого типа данных"""

        res = requests.get(self.URL, headers=self.HEADERS)
        assert 'application/json' in res.headers['Content-Type']

    def test4(self):

        """Проверка возвращаемого кода при указанных пустых параметрах"""

        res = requests.get(self.URL, headers=self.HEADERS, params=self.PARAMS)
        assert res.status_code == 200, f'Возвращаемый статус не равен 200 ({res.status_code})'

    def test5(self):

        """Проверка возвращаемого кода при указанном лимите 0"""

        i = str(0)
        res = requests.get(self.URL + i, headers=self.HEADERS)
        assert res.status_code == 200, f'Возвращаемый статус не равен 200 ({res.status_code})'


