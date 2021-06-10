from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import Course, CourseList, CourseDetail

urlpatterns = [
    path('courses/', CourseList.as_view(), name='courses'),
    path('courses/<int:pk>/', CourseDetail.as_view(), name='course_detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
