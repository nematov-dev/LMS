from django.db import models

from app_common.models import BaseModel
from app_users.models import Student
from app_courses.models import Group

class Month(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'month'
        verbose_name_plural = 'months'

class Part(BaseModel):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.title} - {self.price} UZS"

    class Meta:
        verbose_name = 'Part'
        verbose_name_plural = 'Parts'

class Payment(BaseModel):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='payment')
    group = models.ForeignKey(Group,on_delete=models.CASCADE,related_name='payment')
    month = models.ForeignKey('Month',on_delete=models.CASCADE,related_name='payment')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    parts = models.ManyToManyField(Part, related_name='payment')

    def __str__(self):
        return f"{self.student.user.full_name} - {self.price} UZS ({self.month.title})"
    
    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
