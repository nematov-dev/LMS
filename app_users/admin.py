from django.contrib import admin

from app_users.models import User,Teacher,Student,Worker,Department

admin.site.register([User,Teacher,Student,Worker,Department])
