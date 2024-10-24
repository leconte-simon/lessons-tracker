from rest_framework.viewsets import ModelViewSet

from lessons_tracker.lessons.models import ClassLevel
from lessons_tracker.lessons.serializers.class_level import ClassLevelSerializer


class ClassLevelViewSet(ModelViewSet):
    queryset = ClassLevel.objects.all()
    serializer_class = ClassLevelSerializer
    filterset_fields = "__all__"
