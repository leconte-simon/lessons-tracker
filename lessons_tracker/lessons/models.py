from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator
import django.utils.timezone
from datetime import timedelta


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


class ClassSubject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"


class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(
        ClassSubject, through="LessonToSubjectRelation", related_name="lessons"
    )
    datetime = models.DateTimeField(default=django.utils.timezone.now)
    duration = models.DurationField(default=timedelta(hours=1))
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    paid = models.BooleanField()

    def __str__(self) -> str:
        return f"{self.id} - {self.student.name} - {self.datetime.strftime('%Y-%m-%d %H:%M:%S')}"


class LessonToSubjectRelation(models.Model):
    id = models.AutoField(primary_key=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    subject = models.ForeignKey(ClassSubject, on_delete=models.CASCADE)
