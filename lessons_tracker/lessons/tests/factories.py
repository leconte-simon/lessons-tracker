import factory
import factory.fuzzy
from factory.django import DjangoModelFactory

from lessons_tracker.lessons.models import ClassLevel, Student, ClassSubject


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
