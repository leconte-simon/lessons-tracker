from rest_framework import viewsets
from lessons_tracker.lessons.models import Lesson
from rest_framework.request import Request
from rest_framework.response import Response
from lessons_tracker.lessons.serializers.summary import (
    LessonStatisticsSerializer,
    LessonsStatisticsByMonthSerializer,
)

from django.db.models import Sum, Count, Q
from rest_framework.decorators import action
from datetime import timedelta
from django.db.models.functions import ExtractMonth, ExtractYear
from django.db.models.query import QuerySet


class LessonStatisticsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonStatisticsSerializer
    filterset_fields = ["student"]

    aggregation = {
        "total_paid": Sum("price", filter=Q(paid=True), default=0),
        "total_lessons": Count("id"),
        "total_to_be_paid": Sum("price", filter=Q(paid=False), default=0),
        "total_time": Sum("duration", default=timedelta()),
    }

    def list(self, request: Request) -> Response:
        # Calculate overall lesson statistics
        queryset = self.filter_queryset(self.get_queryset())
        global_data = queryset.aggregate(**self.aggregation)

        # Serialize the statistics
        serializer = self.get_serializer(global_data)

        return Response(serializer.data)

    def retrieve(self, request: Request, pk: int | None = None) -> Response:
        raise NotImplementedError

    @action(methods=["get"], detail=False)
    def trend(self, request: Request) -> Response:
        queryset: QuerySet[Lesson] = self.filter_queryset(self.get_queryset())
        queryset = (
            queryset.annotate(
                month=ExtractMonth("datetime"), year=ExtractYear("datetime")
            )
            .values("month", "year")
            .annotate(**self.aggregation)
            .order_by("year", "month")
        )
        serializer = LessonsStatisticsByMonthSerializer(queryset, many=True)
        return Response(serializer.data)
