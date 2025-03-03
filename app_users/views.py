from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, UpdateAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from drf_yasg.utils import swagger_auto_schema
from rest_framework.pagination import PageNumberPagination

from app_users.permissions import AdminUser
from app_users.serializers import TeacherSerializer, UserSerializer, StudentSerializer, UserAndTeacherSerializer, \
    UserAndStudentSerializer, \
    WorkerSerializer, UserAndWorkerSerializer, UserAllSerializer, DepartmentSerializer, DepartamentAddWorker
from app_users.models import Teacher,Student,Worker,User,Department

class Pagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 50 

#User
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserAllSerializer
    pagination_class = Pagination
    permission_classes = [AdminUser]

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserAllSerializer
    lookup_field = 'id'
    permission_classes = [AdminUser]

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserAllSerializer
    permission_classes = [AdminUser]

class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserAllSerializer
    lookup_field = 'id'
    permission_classes = [AdminUser]

class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserAllSerializer
    lookup_field = 'id'
    permission_classes = [AdminUser]

#Departament
class DepartmentViewSet(viewsets.ViewSet):
    permission_classes = [AdminUser]

    def list(self, request):
        departments = Department.objects.all()
        paginator = Pagination()
        result_page = paginator.paginate_queryset(departments, request)
        serializer = DepartmentSerializer(result_page, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        department = get_object_or_404(Department, pk=pk)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], url_path='create/department')
    @swagger_auto_schema(request_body=DepartmentSerializer)
    def create_department(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'], url_path='update/department')
    def update_department(self, request, pk=None):
        department = get_object_or_404(Department, pk=pk)
        serializer = DepartmentSerializer(department, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'], url_path='delete/department')
    def delete_department(self, request, pk=None):
        department = get_object_or_404(Department, pk=pk)
        department.delete()
        return Response({'status':True,'detail': 'Department deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'], url_path='add-worker')
    @swagger_auto_schema(request_body=DepartamentAddWorker)
    def add_worker(self, request, pk=None):
        department = get_object_or_404(Department, pk=pk)
        serializer = DepartamentAddWorker(data=request.data)

        if serializer.is_valid():
            worker_id = serializer.validated_data['worker_id']
            worker = get_object_or_404(Worker, pk=worker_id)
            worker.department = department
            worker.save()

            return Response({'status':True,'detail': f'Worker {worker.user.phone} added to department {department.title}'},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Teacher
class TeacherListView(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    pagination_class = Pagination
    permission_classes = [AdminUser]

class TeacherUpdateView(UpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    lookup_field = 'id'
    permission_classes = [AdminUser]

class TeacherRetrieveAPIView(RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    lookup_field = 'id'
    permission_classes = [AdminUser]

class TeacherCreateAPIView(APIView):
    permission_classes = [AdminUser]

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
    permission_classes = [AdminUser]

class StudentUpdateView(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'
    permission_classes = [AdminUser]

class StudentRetrieveAPIView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'
    permission_classes = [AdminUser]

class StudentCreateAPIView(APIView):
    permission_classes = [AdminUser]

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
    permission_classes = [AdminUser]

class WorkerUpdateView(UpdateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    lookup_field = 'id'
    permission_classes = [AdminUser]

class WorkerRetrieveAPIView(RetrieveAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    lookup_field = 'id'
    permission_classes = [AdminUser]

class WorkerCreateAPIView(APIView):
    permission_classes = [AdminUser]

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

