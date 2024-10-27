from django.urls import path
from lessons_tracker.lessons.views.student import StudentViewSet
from lessons_tracker.lessons.views.class_level import ClassLevelViewSet
from lessons_tracker.lessons.views.class_subject import ClassSubjectViewSet
from lessons_tracker.lessons.views.lesson import LessonViewSet
from rest_framework import routers
from django.urls import include

router = routers.DefaultRouter()
router.register("students", StudentViewSet)
router.register("class_level", ClassLevelViewSet)
router.register("class_subject", ClassSubjectViewSet)
router.register("lessons", LessonViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
