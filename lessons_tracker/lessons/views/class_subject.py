from lessons_tracker.lessons.models import ClassSubject
from lessons_tracker.lessons.serializers.class_subject import ClassSubjectSerializer
from rest_framework import viewsets


class ClassSubjectViewSet(viewsets.ModelViewSet):
    queryset = ClassSubject.objects.all()
    serializer_class = ClassSubjectSerializer
    filterset_fields = "__all__"
