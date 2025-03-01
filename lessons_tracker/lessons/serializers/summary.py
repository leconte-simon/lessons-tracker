from rest_framework import serializers


class LessonStatisticsSerializer(serializers.Serializer):
    total_lessons = serializers.IntegerField()
    total_paid = serializers.FloatField()
    total_to_be_paid = serializers.FloatField()
    total_time = serializers.DurationField()


class LessonsStatisticsByMonthSerializer(serializers.Serializer):
    month = serializers.IntegerField()
    year = serializers.IntegerField()
    total_lessons = serializers.IntegerField()
    total_paid = serializers.FloatField()
    total_to_be_paid = serializers.FloatField()
    total_time = serializers.DurationField()
