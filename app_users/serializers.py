from rest_framework import serializers
from django.contrib.auth.hashers import make_password


from app_users.models import Teacher, User, Student, Worker,Department

class UserAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","password","full_name","phone")
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

class TeacherSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Teacher
        fields = ('id','user','group', 'cource', 'description')

class StudentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Student
        fields = ('id','user','group', 'cource', 'description')

class WorkerSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Worker
        fields = ('id','user','departments','description')

class DepartamentAddWorker(serializers.Serializer):
    worker_id = serializers.IntegerField()

class UserAndTeacherSerializer(serializers.Serializer):
    user = UserSerializer()
    teacher = TeacherSerializer()

class UserAndStudentSerializer(serializers.Serializer):
    user = UserSerializer()
    student = StudentSerializer()

class UserAndWorkerSerializer(serializers.Serializer):
    user = UserSerializer()
    worker = WorkerSerializer()