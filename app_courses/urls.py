from rest_framework.routers import DefaultRouter
from django.urls import path, include

from app_courses.views import GroupViewSet, SubjectViewSet, TableViewSet, TableTypeViewSet, CourseViewSet

app_name = 'courses'

router = DefaultRouter()
router.register(r'groups', GroupViewSet, basename='group')
router.register(r'subjects', SubjectViewSet, basename='subject')
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'tables', TableViewSet, basename='table')
router.register(r'tabletypes', TableTypeViewSet, basename='tabletype')

urlpatterns = [
    path('', include(router.urls)),
]