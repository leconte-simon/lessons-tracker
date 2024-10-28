from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .factories import ClassLevelFactory
from django.contrib.auth.models import User


class TestClassLevel(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.force_login(user=self.user)

    def test_list_class_level(self) -> None:
        ClassLevelFactory.create_batch(4)
        response = self.client.get("/class_level/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_get_class_level(self) -> None:
        class_level = ClassLevelFactory()
        response = self.client.get(f"/class_level/{class_level.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], class_level.name)

    def test_create_class_level(self) -> None:
        response = self.client.post("/class_level/", {"name": "Level 1"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "Level 1")

    def test_create_class_level_with_invalid_data(self) -> None:
        response = self.client.post("/class_level/", {"name": ""})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_class_level(self) -> None:
        class_level = ClassLevelFactory()
        new_name = "Level 2"
        response = self.client.patch(
            f"/class_level/{class_level.id}/", {"name": new_name}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], new_name)

    def test_delete_class_level(self) -> None:
        class_level = ClassLevelFactory()
        response = self.client.delete(f"/class_level/{class_level.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestUnauthenticatedClassLevel(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_redirects_to_login(self) -> None:
        response = self.client.get("/class_level/")
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        assert response.url == "/accounts/login/?next=/class_level/"
