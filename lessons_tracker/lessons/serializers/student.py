from rest_framework import serializers
from lessons_tracker.lessons.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
