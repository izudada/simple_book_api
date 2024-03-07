from rest_framework.test import APITestCase
from authentication.models import User


class TestAuthenticationModel(APITestCase):

    def test_create_user_succeeds(self):
        user = User.objects.create_user(
            username="tony_medici",
            first_name="John",
            last_name="Python",
            email="tonymedici@gmail.com",
            password="password1234@#"
        )
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, "tonymedici@gmail.com")
        self.assertFalse(user.is_staff)
        self.assertTrue(user.check_password("password1234@#"))

    def test_create_super_user_succeeds(self):
        user = User.objects.create_superuser(
            username="tony_medici",
            first_name="John",
            last_name="Python",
            email="tonymedici@gmail.com",
            password="password1234@#"
        )
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, "tonymedici@gmail.com")
        self.assertTrue(user.is_staff)
        self.assertTrue(user.check_password("password1234@#"))

    def test_for_value_error_when_no_username_arguement_fails(self):
        self.assertRaises(
            ValueError, 
            User.objects.create_user, 
            username="",
            first_name="John",
            last_name="Python",
            email="tonymedici@gmail.com",
            password="password1234@#"
        )
        self.assertRaisesMessage(ValueError, "The given username must be set")

    def test_for_value_error_when_no_email_arguement_fails(self):
        self.assertRaises(
            ValueError, 
            User.objects.create_user, 
            username="tony_medici",
            first_name="John",
            last_name="Python",
            email="",
            password="password1234@!"
        )
        self.assertRaisesMessage(ValueError, "The given email must be set")

    def test_create_super_user_with_no_super_user_is_staff_status_fails(self):
        with self.assertRaisesMessage(ValueError, "Superuser must have is_staff=True."):
            User.objects.create_superuser(
                username="tony_medici",
                first_name="John",
                last_name="Python",
                email="tonymedici@gmail.com",
                password="password1234@#",
                is_staff=False
            )

    def test_create_super_user_with_no_super_user_is_superuser_status_fails(self):
        with self.assertRaisesMessage(ValueError, "Superuser must have is_superuser=True."):
            User.objects.create_superuser(
                username="tony_medici",
                first_name="John",
                last_name="Python",
                email="tonymedici@gmail.com",
                password="password1234@#",
                is_superuser=False
            )
