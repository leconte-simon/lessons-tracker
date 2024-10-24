from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .factories import StudentFactory, ClassLevelFactory

from typing import TypedDict, Any


class FieldValueDict(TypedDict):
    field: str
    value: Any


class TestStudents(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        class_level = ClassLevelFactory()
        self.valid_student_payload = {
            "name": "John Doe",
            "level": class_level.pk,
            "phone_number": "+33612345678",
            "parent_phone_number": "+33612345678",
            "address": "123 Main St",
        }

    def test_list_students(self) -> None:
        StudentFactory.create_batch(4)
        response = self.client.get("/students/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_get_student(self) -> None:
        student = StudentFactory()
        response = self.client.get(f"/students/{student.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], student.name)

    def test_create_student(self) -> None:
        response = self.client.post("/students/", self.valid_student_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], self.valid_student_payload["name"])

    def test_create_student_with_invalid_data(self) -> None:
        field_and_values_to_change: list[FieldValueDict] = [
            {"field": "name", "value": ""},
            {"field": "level", "value": ""},
            {"field": "level", "value": 999},
            {"field": "phone_number", "value": "invalid_phone_number"},
            {"field": "parent_phone_number", "value": "1234"},
        ]
        for field_and_value in field_and_values_to_change:
            payload = self.valid_student_payload.copy()
            payload[field_and_value["field"]] = field_and_value["value"]
            response = self.client.post("/students/", payload)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_student(self) -> None:
        student = StudentFactory()
        new_name = "Jane Doe"
        response = self.client.patch(f"/students/{student.id}/", {"name": new_name})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_student(self) -> None:
        student = StudentFactory()
        response = self.client.delete(f"/students/{student.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_filter_students_by_level(self) -> None:
        level_1 = ClassLevelFactory()
        level_2 = ClassLevelFactory()
        StudentFactory.create_batch(3, level=level_1)
        StudentFactory.create_batch(2, level=level_2)
        response = self.client.get(f"/students/?level={level_1.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        response = self.client.get(f"/students/?level={level_2.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
