from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .factories import LessonFactory, StudentFactory, ClassSubjectFactory
from lessons_tracker.lessons.models import Lesson
import datetime as dt
from django.contrib.auth.models import User


class LessonTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.force_login(user=self.user)

    def test_get_lesson(self) -> None:
        lesson = LessonFactory()
        response = self.client.get(f"/lessons/{lesson.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], lesson.id)

    def test_list_lessons(self) -> None:
        LessonFactory.create_batch(4)
        response = self.client.get("/lessons/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_create_lesson(self) -> None:
        student = StudentFactory()
        class_subject = ClassSubjectFactory()
        response = self.client.post(
            "/lessons/",
            {
                "student": student.pk,
                "subjects": [class_subject.pk, class_subject.pk],
                "price": 20,
                "paid": False,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        lesson = Lesson.objects.get(id=response.data["id"])
        assert (
            lesson.subjects.count() == 1
        )  # Only one many to many relation should be created
        assert lesson.price == 20
        assert (dt.datetime.now(dt.timezone.utc) - lesson.datetime) <= dt.timedelta(
            seconds=5
        )

    def test_update_lesson(self) -> None:
        lesson = LessonFactory()
        new_price = 25
        response = self.client.patch(f"/lessons/{lesson.id}/", {"price": new_price})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["price"], new_price)

        assert Lesson.objects.get(id=lesson.id).price == new_price

    def test_delete_lesson(self) -> None:
        lesson = LessonFactory()
        response = self.client.delete(f"/lessons/{lesson.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        assert not Lesson.objects.filter(id=lesson.id).exists()
