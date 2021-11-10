from django.test import TestCase

from django.contrib.auth import get_user_model
from .models import Status

User = get_user_model()


class StatusTestCase(TestCase):
    username = 'pashaTest'

    def setUp(self):
        user = User.objects.create(username=self.username, email="pasha@test.com")
        user.set_password("testPAsword")
        user.save()

    def test_create_status(self):
        user = User.objects.get(username=self.username)
        obj = Status.objects.create(user=user, content='Test content')
        self.assertEqual(obj.id, 1)
        qs = Status.objects.all()
        self.assertEqual(qs.count(), 1)
