import unittest
from app.core import appointments_app


class TestHome(unittest.TestCase):
    def setUp(self):
        client = appointments_app.test_client()
        client.testing = True
        self.response = client.get('/appointments')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    # def test_content_type(self):
    #     self.assertIn('text/html', self.response.content_type)


if __name__ == '__main__':
    unittest.main()
