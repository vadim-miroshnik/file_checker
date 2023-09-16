from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import File, Log


class FileTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", password="testpass123"
        )

        cls.file = File.objects.create(
            name="test.py", author=cls.user, status=File.FileStatus.CREATED
        )

        cls.log = Log.objects.create(
            file=cls.file,
            log_txt="Test log entry",
        )

    def test_file_listing(self):
        self.assertEqual(f"{self.file.name}", "test.py")
        self.assertEqual(f"{self.file.status}", File.FileStatus.CREATED)

    def test_file_list_view_for_logged_in_user(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test.py")
        self.assertTemplateUsed(response, "home.html")

    def test_file_list_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "%s?next=/" % (reverse("login")))
        response = self.client.get("%s?next=/" % (reverse("login")))
        self.assertContains(response, "Log In")

    def test_file_detail_view_with_permissions(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(self.file.get_absolute_url())
        no_response = self.client.get("/files/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "test.py")
        self.assertContains(response, "Test log entry")
        self.assertTemplateUsed(response, "files_detail.html")
