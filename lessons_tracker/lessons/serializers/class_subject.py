from lessons_tracker.lessons.models import ClassSubject
from rest_framework import serializers


class ClassSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassSubject
        fields = "__all__"
