from django.test import TestCase
from django.contrib.auth import get_user_model
from users.models import User


# Create your tests here.


class UsersManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(password='0000', email='user@1.com', is_active='True')
        self.assertEqual(user.email, 'user@1.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(password='7777', email='user@777.com', )
        self.assertEqual(admin_user.email, 'user@777.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='user@777.com', password='7777', is_superuser=False)