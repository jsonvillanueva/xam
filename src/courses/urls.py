from django.urls import path

from .views import (
    course_create_view,
    course_delete_view,
    course_detail_view,
    courses_view,
)

app_name = "courses"

urlpatterns = [
    path("", courses_view, name="course-list"),
    path("create/", course_create_view, name="course-create"),
    path("<int:id>/", course_detail_view, name="course-detail"),
    path("<int:id>/delete/", course_delete_view, name="course-delete"),
]
