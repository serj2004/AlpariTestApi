import json
import requests


class TestAlpariApi:
    URL = "https://alpari.com/api/ru/forex_instruments/currency_converter/rate/?"

    HEADERS = {"User-Agent": "Test", "Referer": "https://alpari.com"}

    def test_func(self, src, dst):
        res = requests.get(f'{self.URL} src= {src} &dst= {dst}', headers=self.HEADERS)
        body = json.loads(res.content)
        try:
            assert res.status_code == 200
            assert 'application/json' in res.headers['Content-Type']
            assert body["success"] is True
            rate = str(body["data"]["rate"])
            assert rate.isdigit
        except AssertionError:
            return False
        else:
            return True


Tst = TestAlpariApi()
Tst.test_func('EUR', 'USD')
