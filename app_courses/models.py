from django.db import models

from app_common.models import BaseModel


class Course(BaseModel):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

class Subject(BaseModel):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

class TableType(BaseModel):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Table Type'
        verbose_name_plural = 'Table Types'

class Table(BaseModel):
    start_time = models.TimeField()
    finish_time = models.TimeField()
    room = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    type = models.ForeignKey(TableType, on_delete=models.CASCADE, related_name='tables')

    def __str__(self):
        return f"{self.room} ({self.start_time} - {self.finish_time})"

    class Meta:
        verbose_name = 'Table'
        verbose_name_plural = 'Tables'

class Group(BaseModel):
    title = models.CharField(max_length=100)
    worker = models.ForeignKey('app_users.Worker', on_delete=models.CASCADE, related_name='groups',null=True, blank=True)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, related_name='groups')
    active = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    table = models.ForeignKey('Table', on_delete=models.SET_NULL, null=True, blank=True, related_name='groups')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'
