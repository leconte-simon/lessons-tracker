from rest_framework import serializers
from lessons_tracker.lessons.models import ClassLevel


class ClassLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassLevel
        fields = "__all__"
