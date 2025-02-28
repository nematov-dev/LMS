from rest_framework import serializers


from app_users.models import Teacher

class Teacher(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"