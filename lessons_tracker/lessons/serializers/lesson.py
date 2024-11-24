from lessons_tracker.lessons.models import Lesson, ClassSubject
from rest_framework import serializers


class LessonSerializer(serializers.ModelSerializer):
    subjects = serializers.PrimaryKeyRelatedField(
        many=True, queryset=ClassSubject.objects
    )

    class Meta:
        model = Lesson
        fields = "__all__"
