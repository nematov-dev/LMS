from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app_users.views import TeacherCreateAPIView, TeacherListView, TeacherUpdateView, StudentListView, \
    StudentUpdateView, \
    StudentCreateAPIView, WorkerListView, WorkerUpdateView, WorkerCreateAPIView, WorkerRetrieveAPIView, \
    TeacherRetrieveAPIView, StudentRetrieveAPIView, \
    UserListView, UserDetailView, UserCreateView, UserUpdateView, UserDeleteView, DepartmentViewSet, ParentViewSet, \
    TeacherGroupsAPIView, StudentGroupsAPIView, WorkerDepartamentsAPIView

app_name = 'users'

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet, basename='department')

router2 = DefaultRouter()
router2.register(r'parents', ParentViewSet, basename='parent')


urlpatterns = [
    #users
    path('', UserListView.as_view(), name='user-list'), 
    path('user/<int:id>/', UserDetailView.as_view(), name='user-detail'), 
    path('create/user/', UserCreateView.as_view(), name='user-create'), 
    path('update/user/<int:id>/', UserUpdateView.as_view(), name='user-update'), 
    path('delete/user/<int:id>/', UserDeleteView.as_view(), name='user-delete'), 

    #worker
    path('workers/',WorkerListView.as_view(),name="all_workers"),
    path('worker/<int:id>/',WorkerRetrieveAPIView.as_view(),name="worker"),
    path('create/worker/',WorkerCreateAPIView.as_view(),name='add_worker'),
    path('update/worker/<int:id>/',WorkerUpdateView.as_view(),name="update_worker"),
    path('worker-departaments/<int:worker_id>/', WorkerDepartamentsAPIView.as_view(), name="worker_departaments"),

    #teacher
    path('teachers/',TeacherListView.as_view(),name="all_teachers"),
    path('teacher/<int:id>/',TeacherRetrieveAPIView.as_view(),name="teacher"),
    path('create/teacher/',TeacherCreateAPIView.as_view(),name='add_teacher'),
    path('update/teacher/<int:id>/',TeacherUpdateView.as_view(),name="update_teacher"),
    path('teacher-groups/<int:teacher_id>/',TeacherGroupsAPIView.as_view(),name="teacher_groups"),

    #student
    path('students/',StudentListView.as_view(),name="all_students"),
    path('student/<int:id>/',StudentRetrieveAPIView.as_view(),name="student"),
    path('create/student/',StudentCreateAPIView.as_view(),name='add_student'),
    path('update/student/<int:id>/',StudentUpdateView.as_view(),name="update_student"),
    path('student-groups/<int:student_id>/', StudentGroupsAPIView.as_view(), name="student_groups"),

    #department
    path('', include(router.urls)),

    #parent
    path('',include(router2.urls)),

]
