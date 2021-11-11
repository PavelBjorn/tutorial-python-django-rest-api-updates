from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse as api_revers

User = get_user_model()


class UserAPITestCase(APITestCase):
    username = 'JaneDou'

    def setUp(self):
        user = User.objects.create(username="Mr.Dou", email="dou@dou.com")
        user.set_password("Mr.Dou.Password")
        user.save()

    def test_register_user_api_faile(self):
        url = api_revers('api-auth:register')
        data = {
            'username': self.username,
            'email': 'JaneDou@some.come',
            'password': 'some_test_password'
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['password2'][0], 'This field is required.')

    def test_register_user_api(self):
        url = api_revers('api-auth:register')
        data = {
            'username': self.username,
            'email': 'JaneDou@some.come',
            'password': 'some_test_password',
            'password2': 'some_test_password'
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        token_len = len(response.data.get('token', 0))
        self.assertGreater(token_len, 0)

    def test_login_user_api(self):
        url = api_revers('api-auth:login')
        data = {
            'username': "Mr.Dou",
            'password': 'Mr.Dou.Password',
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token_len = len(response.data.get('token', ''))
        self.assertGreater(token_len, 0)

    def test_login_user_api_failed(self):
        url = api_revers('api-auth:login')
        data = {
            'username': "Mr.Dou",
            'password': 'Wrong password',
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        token_len = len(response.data.get('token', ''))
        self.assertEqual(token_len, 0)

    def test_token_login_user_api(self):
        url = api_revers('api-auth:login')
        data = {
            'username': "Mr.Dou",
            'password': 'Mr.Dou.Password',
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = response.data.get('token', None)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        response2 = self.client.post(url, data, format='json')
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response2.data.get('detail', ''), "Already authenticated!")
