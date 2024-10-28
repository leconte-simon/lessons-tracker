from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .factories import ClassSubjectFactory
from lessons_tracker.lessons.models import ClassSubject
from django.contrib.auth.models import User


class TestClassSubject(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.force_login(user=self.user)

    def test_class_subject_list(self) -> None:
        ClassSubjectFactory.create_batch(4)
        response = self.client.get("/class_subject/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_class_subject_detail(self) -> None:
        class_subject = ClassSubjectFactory()
        response = self.client.get(f"/class_subject/{class_subject.pk}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], class_subject.name)

    def test_class_subject_create(self) -> None:
        response = self.client.post("/class_subject/", {"name": "Subject 1"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "Subject 1")
        assert "id" in response.data

    def test_class_subject_update(self) -> None:
        class_subject = ClassSubjectFactory()
        new_name = "Subject 2"
        response = self.client.patch(
            f"/class_subject/{class_subject.pk}/", {"name": new_name}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], new_name)

    def test_class_subject_delete(self) -> None:
        class_subject = ClassSubjectFactory()
        response = self.client.delete(f"/class_subject/{class_subject.pk}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        assert not ClassSubject.objects.filter(pk=class_subject.pk).exists()
