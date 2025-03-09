from django.contrib import admin

from app_courses.models import Group, Course, Subject, TableType, Table, Homework, HomeworkSubmission, HomeworkReview

admin.site.register([Group,Course,Subject,TableType,Table,Homework,HomeworkSubmission,HomeworkReview])
