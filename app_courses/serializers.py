from rest_framework import serializers

from app_courses.models import Group, Subject, Course, Table, TableType


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'

class TableTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableType
        fields = '__all__'

class GroupAddStudent(serializers.Serializer):
    student_id = serializers.IntegerField()

class GroupAddTeacher(serializers.Serializer):
    teacher_id = serializers.IntegerField()