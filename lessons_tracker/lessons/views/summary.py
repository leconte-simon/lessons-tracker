from rest_framework import viewsets
from lessons_tracker.lessons.models import Lesson
from rest_framework.request import Request
from rest_framework.response import Response
from lessons_tracker.lessons.serializers.summary import LessonStatisticsSerializer

from django.db.models import Sum, Count, Q


class LessonStatisticsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonStatisticsSerializer
    filterset_fields = ["student"]

    def list(self, request: Request) -> Response:
        # Calculate overall lesson statistics
        queryset = self.filter_queryset(self.get_queryset())
        global_data = queryset.aggregate(
            total_paid=Sum("price", filter=Q(paid=True), default=0),
            total_lessons=Count("id"),
            total_to_be_paid=Sum("price", filter=Q(paid=False), default=0),
        )

        # Serialize the statistics
        serializer = self.get_serializer(global_data)

        return Response(serializer.data)

    def retrieve(self, request: Request, pk: int | None = None) -> Response:
        raise NotImplementedError
