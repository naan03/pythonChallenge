import unittest
import requests

class TestCsvGenerator(unittest.TestCase):

    def test_pass(self):

        url = "http://127.0.0.1:5000/file"
        data = {'file_data': 'valuevaluevaluevaluevaluevaluevaluevaluevaluevaluevaluevalue'}

        with requests.post(url, data=data) as response:
            print(response)
            assert response.status_code == 200

if __name__ == '__main__':
    unittest.main()