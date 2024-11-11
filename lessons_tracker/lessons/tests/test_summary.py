from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .factories import LessonFactory

from django.contrib.auth.models import User


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.force_login(user=self.user)

    def test_summary(self) -> None:
        response = self.client.get("/summary/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["total_lessons"], 0)
        self.assertEqual(response.data["total_to_be_paid"], 0)
        self.assertEqual(response.data["total_paid"], 0)

    def test_summary_with_paid_lesson(self) -> None:
        lesson = LessonFactory(paid=True)
        response = self.client.get("/summary/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["total_lessons"], 1)
        self.assertEqual(response.data["total_to_be_paid"], 0)
        self.assertAlmostEqual(response.data["total_paid"], lesson.price)

    def test_summary_with_unpaid_lesson(self) -> None:
        lesson = LessonFactory(paid=False)
        response = self.client.get("/summary/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["total_lessons"], 1)
        self.assertAlmostEqual(response.data["total_to_be_paid"], lesson.price)
        self.assertEqual(response.data["total_paid"], 0)

    def test_summary_with_paid_and_unpaid_lesson(self) -> None:
        paid_lessons = LessonFactory.create_batch(3, paid=True)
        unpaid_lessons = LessonFactory.create_batch(2, paid=False)
        response = self.client.get("/summary/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["total_lessons"], 5)
        self.assertAlmostEqual(
            response.data["total_to_be_paid"],
            sum(lesson.price for lesson in unpaid_lessons),
        )
        self.assertAlmostEqual(
            response.data["total_paid"], sum(lesson.price for lesson in paid_lessons)
        )

    def test_filter_summary_by_student(self) -> None:
        lesson_1 = LessonFactory(paid=True)
        LessonFactory()
        response = self.client.get(f"/summary/?student={lesson_1.student.pk}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["total_lessons"], 1)
        self.assertEqual(response.data["total_to_be_paid"], 0)
        self.assertAlmostEqual(response.data["total_paid"], lesson_1.price)

    def test_summary_trend_empty(self) -> None:
        response = self.client.get("/summary/trend/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_summary_trend(self) -> None:
        lesson_april = LessonFactory(datetime="2023-04-01", paid=True)
        lesson_may = LessonFactory(datetime="2023-05-01", paid=True)
        response = self.client.get("/summary/trend/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["month"], 4)
        self.assertEqual(response.data[0]["year"], 2023)
        self.assertEqual(response.data[0]["total_lessons"], 1)
        self.assertEqual(response.data[0]["total_to_be_paid"], 0)
        self.assertAlmostEqual(response.data[0]["total_paid"], lesson_april.price)
        self.assertEqual(response.data[1]["month"], 5)
        self.assertEqual(response.data[1]["year"], 2023)
        self.assertEqual(response.data[1]["total_lessons"], 1)
        self.assertEqual(response.data[1]["total_to_be_paid"], 0)
        self.assertAlmostEqual(response.data[1]["total_paid"], lesson_may.price)
