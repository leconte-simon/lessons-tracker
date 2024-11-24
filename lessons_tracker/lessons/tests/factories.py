import factory
import factory.fuzzy
from factory.django import DjangoModelFactory

from lessons_tracker.lessons.models import (
    ClassLevel,
    Student,
    ClassSubject,
    Lesson,
    LessonToSubjectRelation,
)

import datetime as dt


class ClassLevelFactory(DjangoModelFactory):
    class Meta:
        model = ClassLevel

    name = factory.fuzzy.FuzzyText()


class StudentFactory(DjangoModelFactory):
    class Meta:
        model = Student

    name = factory.fuzzy.FuzzyText()
    level = factory.SubFactory(ClassLevelFactory)
    phone_number = factory.Faker("phone_number")
    parent_phone_number = factory.fuzzy.FuzzyText()
    address = factory.fuzzy.FuzzyText()


class ClassSubjectFactory(DjangoModelFactory):
    class Meta:
        model = ClassSubject

    name = factory.fuzzy.FuzzyText()


class LessonFactory(DjangoModelFactory):
    class Meta:
        model = Lesson

    student = factory.SubFactory(StudentFactory)
    datetime = factory.fuzzy.FuzzyDateTime(
        start_dt=dt.datetime(2022, 1, 1, tzinfo=dt.timezone.utc)
    )
    price = factory.fuzzy.FuzzyFloat(low=0, high=100)
    paid = factory.fuzzy.FuzzyChoice([True, False])


class LessonToSubjectRelationFactory(DjangoModelFactory):
    class Meta:
        model = LessonToSubjectRelation

    lesson = factory.SubFactory(LessonFactory)
    subject = factory.SubFactory(ClassSubjectFactory)
