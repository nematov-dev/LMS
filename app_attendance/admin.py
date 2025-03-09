from django.contrib import admin

from app_attendance.models import Status, Attendance

admin.site.register([Status,Attendance])
