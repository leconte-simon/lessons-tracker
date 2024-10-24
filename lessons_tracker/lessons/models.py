from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class ClassLevel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    level = models.ForeignKey(ClassLevel, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(null=True, blank=True)
    parent_phone_number = PhoneNumberField(null=True, blank=True)

    address = models.TextField(null=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"
