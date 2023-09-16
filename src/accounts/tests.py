from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse

from .views import SignUpView


class UsersManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser",
            password="testpass1234",
        )
        self.assertEqual(user.username, "testuser")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="testsuperuser",
            password="testpass1234",
        )
        self.assertEqual(admin_user.username, "testsuperuser")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupPageTests(TestCase):
    def test_signup_template(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")
        self.assertContains(response, "Sign Up")
        self.assertNotContains(response, "Hi there! I should not be on the page.")

    def test_signup_form(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "testuser",
                "password1": "testpass123",
                "password2": "testpass123",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, "testuser")

    def test_signup_view(self):
        view = resolve("/accounts/signup/")
        self.assertEqual(view.func.__name__, SignUpView.as_view().__name__)
