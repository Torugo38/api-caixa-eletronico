import unittest
from app import create_app

class SaqueTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()
        self.app.testing = True

    def test_saque(self):
        response = self.app.post('/api/saque', json={'valor': 380})
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['100'], 3)
        self.assertEqual(data['50'], 1)
        self.assertEqual(data['20'], 1)
        self.assertEqual(data['10'], 1)
        self.assertEqual(data['5'], 0)
        self.assertEqual(data['2'], 0)

if __name__ == '__main__':
    unittest.main()
