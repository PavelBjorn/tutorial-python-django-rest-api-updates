from django.test import TestCase

from django.contrib.auth import get_user_model

User = get_user_model()


class UserTestCase(TestCase):
    username = 'pashaTest'

    def setUp(self):
        user = User.objects.create(username=self.username, email="pasha@test.com")
        user.set_password("testPAsword")
        user.save()

    def test_create_user(self):
        qs = User.objects.filter(username=self.username)
        self.assertEqual(qs.count(), 1)

