from django.urls import path
from lessons_tracker.lessons.views.students import StudentViewSet
from lessons_tracker.lessons.views.class_level import ClassLevelViewSet
from rest_framework import routers
from django.urls import include

router = routers.DefaultRouter()
router.register("students", StudentViewSet)
router.register("class_level", ClassLevelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
