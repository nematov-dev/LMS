from django.urls import path,include
from rest_framework.routers import DefaultRouter


from app_users.views import TeacherCreateAPIView,TeacherListView,TeacherUpdateView,StudentListView,StudentUpdateView,\
                            StudentCreateAPIView,WorkerListView,WorkerUpdateView,WorkerCreateAPIView,WorkerRetrieveAPIView,TeacherRetrieveAPIView,StudentRetrieveAPIView,\
                            UserViewSet

app_name = 'users'

router = DefaultRouter()
router.register(r'users',UserViewSet, basename='user')

urlpatterns = [
    #users
    path('', include(router.urls)),

    #worker
    path('workers/',WorkerListView.as_view(),name="all_workers"),
    path('worker/<int:id>/',WorkerRetrieveAPIView.as_view(),name="worker"),
    path('create/worker/',WorkerCreateAPIView.as_view(),name='add_worker'),
    path('update/worker/<int:id>/',WorkerUpdateView.as_view(),name="update_worker"),

    #teacher
    path('teachers/',TeacherListView.as_view(),name="all_teachers"),
    path('teacher/<int:id>/',TeacherRetrieveAPIView.as_view(),name="teacher"),
    path('create/teacher/',TeacherCreateAPIView.as_view(),name='add_teacher'),
    path('update/teacher/<int:id>/',TeacherUpdateView.as_view(),name="update_teacher"),

    #student
    path('students/',StudentListView.as_view(),name="all_students"),
    path('student/<int:id>/',StudentRetrieveAPIView.as_view(),name="student"),
    path('create/student/',StudentCreateAPIView.as_view(),name='add_student'),
    path('update/student/<int:id>/',StudentUpdateView.as_view(),name="update_student"),
]
