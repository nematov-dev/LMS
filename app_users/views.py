from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,UpdateAPIView,RetrieveAPIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from drf_yasg.utils import swagger_auto_schema
from rest_framework.pagination import PageNumberPagination


from app_users.serializers import TeacherSerializer,UserSerializer,StudentSerializer,UserAndTeacherSerializer,UserAndStudentSerializer, \
                                  WorkerSerializer,UserAndWorkerSerializer
from app_users.models import Teacher,Student,Worker,User

class Pagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 50 

#User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = Pagination

#Teacher
class TeacherListView(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    pagination_class = Pagination

class TeacherUpdateView(UpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    lookup_field = 'id'

class TeacherRetrieveAPIView(RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    lookup_field = 'id'

class TeacherCreateAPIView(APIView):
    @swagger_auto_schema(request_body=UserAndTeacherSerializer)
    def post(self, request):
        user_data = request.data.get('user', {})
        user_serializer = UserSerializer(data=user_data)

        if user_serializer.is_valid():
            user = user_serializer.save(is_worker=True)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        teacher_data = request.data.get('teacher', {})   
        teacher_serializer = TeacherSerializer(data=teacher_data)

        if teacher_serializer.is_valid():
            teacher = teacher_serializer.save(user=user)
            return Response(TeacherSerializer(teacher).data, status=status.HTTP_201_CREATED)
        else:
            user.delete()
            return Response(teacher_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Student
class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = Pagination

class StudentUpdateView(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'

class StudentRetrieveAPIView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'

class StudentCreateAPIView(APIView):
    @swagger_auto_schema(request_body=UserAndStudentSerializer)
    def post(self, request):
        user_data = request.data.get('user', {})
        user_serializer = UserSerializer(data=user_data)

        if user_serializer.is_valid():
            user = user_serializer.save(is_student=True)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        student_data = request.data.get('student', {})   
        student_serializer = StudentSerializer(data=student_data)

        if student_serializer.is_valid():
            student = student_serializer.save(user=user)
            return Response(StudentSerializer(student).data, status=status.HTTP_201_CREATED)
        else:
            user.delete()
            return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Worker
class WorkerListView(ListAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    pagination_class = Pagination

class WorkerUpdateView(UpdateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    lookup_field = 'id'

class WorkerRetrieveAPIView(RetrieveAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    lookup_field = 'id'


class WorkerCreateAPIView(APIView):
    @swagger_auto_schema(request_body=UserAndWorkerSerializer)
    def post(self, request):
        user_data = request.data.get('user', {})
        user_serializer = UserSerializer(data=user_data)

        if user_serializer.is_valid():
            user = user_serializer.save(is_worker=True)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        worker_data = request.data.get('worker', {})   
        worker_serializer = WorkerSerializer(data=worker_data)

        if worker_serializer.is_valid():
            worker = worker_serializer.save(user=user)
            return Response(WorkerSerializer(worker).data, status=status.HTTP_201_CREATED)
        else:
            user.delete()
            return Response(worker_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

