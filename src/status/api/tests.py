import io

from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse as api_revers
from status.models import Status
import os
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile

User = get_user_model()


class StatusAPITestCase(APITestCase):
    default_username = 'JaneDou'
    default_password = 'Mr.Dou.Password'

    def loginUser(self, username=default_username, password=default_password):
        url = api_revers('api-auth:login')
        data = {
            'username': username,
            'password': password
        }
        response = self.client.post(url, data, format='json')
        print(response.data)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + response.data.get('token'))
        return response

    def postStatus(self):
        url = api_revers('api-status:list')
        data = {
            'content': 'POST test content'
        }
        return self.client.post(url, data, format='json')

    def putStatus(self, id):
        url = api_revers('api-status:detail', kwargs={'id': id})
        detail_data = {
            'content': 'PUT test data'
        }
        return self.client.put(url, detail_data, format='json')

    def deleteStatus(self, id):
        url = api_revers('api-status:detail', kwargs={'id': id})
        return self.client.delete(url, format='json')

    def setUp(self):
        user = User.objects.create(username=self.default_username, email="dou@dou.com")
        user.set_password(self.default_password)
        user.save()
        status_obj = Status.objects.create(user=user, content='Test content!')

    def test_statuses(self):
        self.assertEqual(Status.objects.count(), 1)

    def test_status_POST_successed(self):
        self.loginUser()
        response = self.postStatus()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg="POST status code")

        id = response.data.get('id', None)
        self.assertEqual(Status.objects.filter(id=id).count(), 1, msg="Try to find Status model in database")

    def test_status_PUT_successed(self):
        self.loginUser()
        post_response = self.postStatus()
        id = post_response.data.get('id', None)

        put_response = self.putStatus(id=id)
        self.assertEqual(put_response.status_code, second=status.HTTP_200_OK, msg="PUT status code")
        self.assertEqual(
            Status.objects.get(id=id).content,
            put_response.data.get('content', None),
            msg="PUT request didn't update Status content"
        )

    def test_status_GET_successed(self):
        self.loginUser()
        post_response = self.postStatus()
        id = post_response.data.get('id', None)
        db_status = Status.objects.get(id=id)

        url = api_revers('api-status:detail', kwargs={'id': id})
        get_response = self.client.get(url)
        self.assertEqual(get_response.status_code, second=status.HTTP_200_OK, msg="GET status code")
        self.assertEqual(
            get_response.data.get('id', None),
            db_status.id,
            msg="GET request return wrong Status"
        )
        self.assertEqual(
            get_response.data.get('content', None),
            db_status.content,
            msg="GET request din't respond with same content"
        )

    def test_status_DELETE_successed(self):
        self.loginUser()
        post_response = self.postStatus()
        id = post_response.data.get('id', None)

        delete_response = self.deleteStatus(id=id)
        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT, 'DELETE status')

    def test_status_should_failed_POST_without_token(self):
        response = self.postStatus()
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_status_should_failed_PUT_without_token(self):
        self.loginUser()
        post_response = self.postStatus()
        self.client.credentials(HTTP_AUTHORIZATION='')
        put_response = self.putStatus(id=post_response.data.get('id', None))
        self.assertEqual(put_response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_status_should_failed_DELETE_without_token(self):
        self.loginUser()
        post_response = self.postStatus()
        self.client.credentials(HTTP_AUTHORIZATION='')
        delete_response = self.deleteStatus(id=post_response.data.get('id', None))
        self.assertEqual(delete_response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_status_POST_image(self):
        self.loginUser()
        url = api_revers('api-status:list')

        bytes = io.BytesIO()
        # (format, (w,h), (RGB))
        image = Image.new('RGB', (800, 1200), (255, 0, 0))
        image.save(bytes, "jpeg")
        tmp_file = SimpleUploadedFile("test.jpg", bytes.getvalue())

        data = {
            'content': "Test image content",
            'image': tmp_file
        }
        response = self.client.post(url, data, format='multipart')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Status.objects.filter(id=response.data.get('id', None)).count(), 1)
        self.assertIsNotNone(response.data.get('image', None))
