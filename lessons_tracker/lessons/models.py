from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Levels(models.TextChoices):
    SIXIEME = "6e"
    CINQUIEME = "5e"
    QUATRIEME = "4e"
    TROISIEME = "3e"
    SECONDE = "2e"
    PREMIERE = "1ere"
    TERMINALE = "Term"
    BACPLUS1 = "Bac+1"
    BACPLUS2 = "Bac+2"
    BACPLUS3 = "Bac+3"
    BACPLUS4 = "Bac+4"
    BACPLUS5 = "Bac+5"


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.TextField()
    level = models.CharField(
        max_length=10,
        choices=Levels.choices,
        null=True,
    )
    phone_number = PhoneNumberField(null=True, blank=True)
    parent_phone_number = PhoneNumberField(null=True, blank=True)

    address = models.TextField(null=True)

    def __str__(self) -> str:
        return f"{self.student_id} - {self.name}"
