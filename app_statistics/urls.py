from django.urls import path

from app_statistics.views import StudentFilterView, TeacherFilterView, GroupFilterView, CourseFilterView, \
    AttendanceFilterView, PaymentFilterView

app_name = 'statistics'

urlpatterns = [
    path('students-statistic/', StudentFilterView.as_view(), name='recent-students'),
    path('teachers-statistic/', TeacherFilterView.as_view(), name='teachers-statistic'),
    path('groups-statistics',GroupFilterView.as_view(), name='groups-statistics'),
    path('courses-statistics',CourseFilterView.as_view(), name='courses-statistics'),
    path('attendance-statistics',AttendanceFilterView.as_view(), name='attendance-statistics'),
    path('payments-statistics',PaymentFilterView.as_view(), name='payments-statistics'),

]