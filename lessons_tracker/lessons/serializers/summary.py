from rest_framework import serializers


class LessonStatisticsSerializer(serializers.Serializer):
    total_lessons = serializers.IntegerField()
    total_paid = serializers.FloatField()
    total_to_be_paid = serializers.FloatField()
