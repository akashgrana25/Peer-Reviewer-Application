from app import app
import unittest
import json


class FlaskTestCase(unittest.TestCase):

    # Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='text/javascript')
        self.assertEqual(response.status_code, 200)

    # Ensure that the index route loads correctly
    def test_index_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='text/javascript')
        self.assertTrue(b'Peer Video Review Application' in response.data)

    # Ensure that index page behaves correctly when values provided are valid
    def test_index_correct_login(self):
        tester = app.test_client(self)
        response = tester.post('/compute', data=dict(m=4, n=2), follow_redirects=True)
        str_to_dict = json.loads(response.data.decode())
        self.assertDictEqual(str_to_dict, {"0": [1, 2], "2": [3, 0], "3": [0, 1], "1": [2, 3]})


if __name__ == '__main__':
    unittest.main()
