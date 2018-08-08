import unittest

class TestGetJWTToken(unittest.TestCase):

    def test_response(self):
        imgy_client = ApiClient(username='pirvan.cristiani@gmail.com', password='4yq4ygvqfn5nmnqmyxzfbstdycuewvyt')
        token = imgy_client.download_file('bdk183ciotqg01a9arng')

        self.assertTrue(len(token) > 0, 'token  cannot be empty')
