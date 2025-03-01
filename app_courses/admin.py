from django.contrib import admin

from app_courses.models import Group,Course,Subject,TableType,Table

admin.site.register([Group,Course,Subject,TableType,Table])
