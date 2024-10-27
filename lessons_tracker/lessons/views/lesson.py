from lessons_tracker.lessons.models import Lesson
from lessons_tracker.lessons.serializers.lesson import LessonSerializer
from rest_framework import viewsets


class LessonViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    filterset_fields = "__all__"
