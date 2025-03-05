from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from app_courses.models import Group, Subject, Course, Table, TableType
from app_common.permissions import AdminUser
from app_common.pagination import Pagination
from app_courses.serializers import GroupSerializer, GroupAddStudent, GroupAddTeacher, SubjectSerializer, \
    CourseSerializer, TableSerializer, TableTypeSerializer
from app_users.models import Student, Teacher

#Group
class GroupViewSet(viewsets.ViewSet):
    permission_classes = [AdminUser]

    def list(self, request):
        groups = Group.objects.all()
        paginator = Pagination()
        result_page = paginator.paginate_queryset(groups, request)
        serializer = GroupSerializer(result_page, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        group = get_object_or_404(Group, pk=pk)
        serializer = GroupSerializer(group)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], url_path='create/group')
    @swagger_auto_schema(request_body=GroupSerializer)
    def create_group(self, request):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'], url_path='update/group')
    def update_group(self, request, pk=None):
        department = get_object_or_404(Group, pk=pk)
        serializer = GroupSerializer(department, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'], url_path='delete/group')
    def delete_group(self, request, pk=None):
        group = get_object_or_404(Group, pk=pk)
        group.delete()
        return Response({'status':True,'detail': 'Group muaffaqiyatli uchirildi'}, status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'], url_path='add-student')
    @swagger_auto_schema(request_body=GroupAddStudent,)
    def add_student(self, request, pk=None):
        group = get_object_or_404(Group, pk=pk)
        serializer = GroupAddStudent(data=request.data)

        if serializer.is_valid():
            student_id = serializer.validated_data['student_id']
            student = get_object_or_404(Student, pk=student_id)
            student.group.add(group)
            student.save()

            return Response({'status':True,'detail': f'Student {student.user.phone} added to group {group.title}'},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'], url_path='add-teacher')
    @swagger_auto_schema(request_body=GroupAddTeacher, )
    def add_teacher(self, request, pk=None):
        group = get_object_or_404(Group, pk=pk)
        serializer = GroupAddTeacher(data=request.data)

        if serializer.is_valid():
            teacher_id = serializer.validated_data['teacher_id']
            teacher = get_object_or_404(Teacher, pk=teacher_id)
            teacher.group.add(group)
            teacher.save()

            return Response(
                {'status': True, 'detail': f'Teacher {teacher.user.phone} added to group {group.title}'},
                status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Subject
class SubjectViewSet(viewsets.ViewSet):
    permission_classes = [AdminUser]

    def list(self, request):
        subjects = Subject.objects.all()
        paginator = Pagination()
        result_page = paginator.paginate_queryset(subjects, request)
        serializer = SubjectSerializer(result_page, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        subject = get_object_or_404(Subject, pk=pk)
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], url_path='create/subject')
    @swagger_auto_schema(request_body=SubjectSerializer)
    def create_subject(self, request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'], url_path='update/subject')
    def update_subject(self, request, pk=None):
        subject = get_object_or_404(Subject, pk=pk)
        serializer = SubjectSerializer(subject, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'], url_path='delete/subject')
    def delete_subject(self, request, pk=None):
        subject = get_object_or_404(Subject, pk=pk)
        subject.delete()
        return Response({'status':True,'detail': 'Subject muaffaqiyatli uchirildi'}, status=status.HTTP_204_NO_CONTENT)

#course
class CourseViewSet(viewsets.ViewSet):
    permission_classes = [AdminUser]

    def list(self, request):
        courses = Course.objects.all()
        paginator = Pagination()
        result_page = paginator.paginate_queryset(courses, request)
        serializer = CourseSerializer(result_page, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        course = get_object_or_404(Course, pk=pk)
        serializer = SubjectSerializer(course)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], url_path='create/course')
    @swagger_auto_schema(request_body=CourseSerializer)
    def create_course(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'], url_path='update/course')
    def update_course(self, request, pk=None):
        course = get_object_or_404(Subject, pk=pk)
        serializer = CourseSerializer(course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'], url_path='delete/course')
    def delete_course(self, request, pk=None):
        course = get_object_or_404(Course, pk=pk)
        course.delete()
        return Response({'status':True,'detail': 'Cource muaffaqiyatli uchirildi'}, status=status.HTTP_204_NO_CONTENT)

#Table
class TableViewSet(viewsets.ViewSet):
    permission_classes = [AdminUser]

    def list(self, request):
        tables = Table.objects.all()
        paginator = Pagination()
        result_page = paginator.paginate_queryset(tables, request)
        serializer = TableSerializer(result_page, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        table = get_object_or_404(Table, pk=pk)
        serializer = TableSerializer(table)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], url_path='create/table')
    @swagger_auto_schema(request_body=TableSerializer)
    def create_table(self, request):
        serializer = TableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'], url_path='update/table')
    def update_table(self, request, pk=None):
        table = get_object_or_404(Table, pk=pk)
        serializer = TableSerializer(table, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'], url_path='delete/table')
    def delete_table(self, request, pk=None):
        table = get_object_or_404(Table, pk=pk)
        table.delete()
        return Response({'status':True,'detail': 'Table muaffaqiyatli uchirildi'}, status=status.HTTP_204_NO_CONTENT)

class TableViewSet(viewsets.ViewSet):
    permission_classes = [AdminUser]

    def list(self, request):
        tables = Table.objects.all()
        paginator = Pagination()
        result_page = paginator.paginate_queryset(tables, request)
        serializer = TableSerializer(result_page, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        table = get_object_or_404(Table, pk=pk)
        serializer = TableSerializer(table)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], url_path='create/table')
    @swagger_auto_schema(request_body=TableSerializer)
    def create_table(self, request):
        serializer = TableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'], url_path='update/table')
    def update_table(self, request, pk=None):
        table = get_object_or_404(Table, pk=pk)
        serializer = TableSerializer(table, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'], url_path='delete/table')
    def delete_table(self, request, pk=None):
        table = get_object_or_404(Table, pk=pk)
        table.delete()
        return Response({'status':True,'detail': 'Table muaffaqiyatli uchirildi'}, status=status.HTTP_204_NO_CONTENT)

class TableTypeViewSet(viewsets.ViewSet):
    permission_classes = [AdminUser]

    def list(self, request):
        tabletypes = TableType.objects.all()
        paginator = Pagination()
        result_page = paginator.paginate_queryset(tabletypes, request)
        serializer = TableTypeSerializer(result_page, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        tabletype = get_object_or_404(TableType, pk=pk)
        serializer = TableTypeSerializer(tabletype)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], url_path='create/tabletype')
    @swagger_auto_schema(request_body=TableTypeSerializer)
    def create_tabletype(self, request):
        serializer = TableTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'], url_path='update/tabletype')
    def update_tabletype(self, request, pk=None):
        tabletype = get_object_or_404(TableType, pk=pk)
        serializer = TableTypeSerializer(tabletype, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'], url_path='delete/tabletype')
    def delete_tabletype(self, request, pk=None):
        tabletype = get_object_or_404(TableType, pk=pk)
        tabletype.delete()
        return Response({'status':True,'detail': 'TableType muaffaqiyatli uchirildi'}, status=status.HTTP_204_NO_CONTENT)

