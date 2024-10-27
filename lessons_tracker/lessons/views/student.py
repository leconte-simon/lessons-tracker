from rest_framework import viewsets
from lessons_tracker.lessons.models import Student
from lessons_tracker.lessons.serializers.student import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filterset_fields = "__all__"
