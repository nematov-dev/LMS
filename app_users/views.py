from calendar import month_name
from collections import defaultdict

from drf_yasg import openapi
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, UpdateAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from drf_yasg.utils import swagger_auto_schema

from app_attendance.models import Attendance
from app_attendance.serializers import AttendanceSerializer
from app_common.permissions import AdminUser, AdminOrOwner, AdminOrTeacher, AdminOrStudent
from app_common.pagination import Pagination, StudentAttendancePagination
from app_courses.models import Group
from app_courses.serializers import GroupSerializer
from app_users.serializers import TeacherSerializer, UserSerializer, StudentSerializer, UserAndTeacherSerializer, \
    UserAndStudentSerializer, ParentSerializer, UserAllSerializer, GetStudentsByIdsSerializer, \
    GetTeachersByIdsSerializer, SuperUserSerializer
from app_users.models import Teacher,Student,User,Parent


#User

class CreateSuperAdminView(APIView):
    permission_classes = [AdminUser]

    @swagger_auto_schema(request_body=SuperUserSerializer)
    def post(self, request):
        serializer = SuperUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Superadmin successfully created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
    permission_classes = [AdminOrOwner]

class GetTeachersByIds(APIView):
    permission_classes = [AdminUser]
    @swagger_auto_schema(request_body=GetTeachersByIdsSerializer)
    def post(self, request):
        teacher_ids = request.data.get("teacher_ids", [])

        if not teacher_ids or not isinstance(teacher_ids, list):
            return Response({"error": "teacher_ids ro‘yxati bo‘lishi kerak"}, status=status.HTTP_400_BAD_REQUEST)

        teachers = Teacher.objects.filter(id__in=teacher_ids)
        serializer = TeacherSerializer(teachers, many=True)

        return Response({"teachers": serializer.data}, status=status.HTTP_200_OK)

class TeacherCreateAPIView(APIView):
    permission_classes = [AdminUser]

    @swagger_auto_schema(request_body=UserAndTeacherSerializer)
    def post(self, request):
        user_data = request.data.get('user', {})
        user_serializer = UserSerializer(data=user_data)

        if user_serializer.is_valid():
            user = user_serializer.save(is_teacher=True)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        teacher_data = request.data.get('teacher', {})   
        teacher_serializer = TeacherSerializer(data=teacher_data)

        if teacher_serializer.is_valid():
            phone = user_data.get('phone')
            user_t = User.objects.get(phone=phone)
            teacher_serializer.validated_data['user'] = user_t
            teacher_serializer.save()
            return Response(teacher_serializer.data, status=status.HTTP_201_CREATED)

        else:
            user.delete()
            return Response(teacher_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherGroupsAPIView(APIView):
    permission_classes = [AdminOrOwner]

    def get(self, request, teacher_id):
        try:
            teacher = Teacher.objects.get(id=teacher_id)
        except Teacher.DoesNotExist:
            return Response({"error": "Teacher not found"}, status=404)

        groups = teacher.groups.all()
        serializer = GroupSerializer(groups, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class TeacherGroupDetailAPIView(APIView):
    permission_classes = [IsAuthenticated,AdminOrTeacher]

    def get(self, request, teacher_id, group_id):
        if not request.user.is_admin and (
                not hasattr(request.user, 'teacher') or request.user.teacher.id != teacher_id):
            return Response(
                {"detail": "Siz faqat o‘z guruhlaringizni ko‘rishingiz mumkin!"},
                status=status.HTTP_403_FORBIDDEN
            )
        try:
            # O'qituvchiga tegishli guruhni topamiz
            group = Group.objects.get(id=group_id, teacher__id=teacher_id)
            students = Student.objects.filter(group=group)

            # Ma’lumotlarni serializatsiya qilish
            group_data = GroupSerializer(group).data
            students_data = StudentSerializer(students, many=True).data

            return Response({
                "group": group_data,
                "students": students_data
            }, status=status.HTTP_200_OK)

        except Group.DoesNotExist:
            return Response({"detail": "Guruh topilmadi yoki bu o'qituvchiga tegishli emas."}, status=status.HTTP_404_NOT_FOUND)

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
    permission_classes = [AdminOrOwner]


class GetStudentsByIds(APIView):
    permission_classes = [AdminUser]
    @swagger_auto_schema(request_body=GetStudentsByIdsSerializer)
    def post(self, request):
        student_ids = request.data.get("student_ids", [])

        if not student_ids or not isinstance(student_ids, list):
            return Response({"error": "student_ids ro‘yxati bo‘lishi kerak"}, status=status.HTTP_400_BAD_REQUEST)

        students = Student.objects.filter(id__in=student_ids)
        serializer = StudentSerializer(students, many=True)

        return Response({"students": serializer.data}, status=status.HTTP_200_OK)


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
            phone = user_data.get('phone')
            user_s = User.objects.get(phone=phone)
            student_serializer.validated_data['user'] = user_s
            student = student_serializer.save()
        else:
            user.delete()
            return Response(student_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        parent_data = request.data.get('parent', {})
        parent_serializer = ParentSerializer(data=parent_data)

        if parent_serializer.is_valid():
            parent = parent_serializer.save()
            parent.students.add(student)
            return Response(parent_serializer.data, status=status.HTTP_201_CREATED)

        else:
            user.delete()
            return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentGroupsAPIView(APIView):
    permission_classes = [AdminOrOwner]
    def get(self, request, student_id):
        try:
            student = Student.objects.get(id=student_id)
        except Teacher.DoesNotExist:
            return Response({"error": "Student not found"}, status=404)

        groups = Group.objects.filter(g_student=student)
        serializer = GroupSerializer(groups, many=True)

        return Response(serializer.data, status=200)


class StudentAttendanceListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="page",
                in_=openapi.IN_QUERY,
                description="Page number for pagination",
                type=openapi.TYPE_INTEGER
            ),
            openapi.Parameter(
                name="page_size",
                in_=openapi.IN_QUERY,
                description="Number of records per page",
                type=openapi.TYPE_INTEGER
            ),
        ],
        responses={200: openapi.Response("Success", AttendanceSerializer(many=True))}
    )

    def get(self, request, student_id):
        # Foydalanuvchi faqat o‘z ma'lumotlarini ko‘rsin
        if hasattr(request.user, 'student') and request.user.student.id != int(student_id) and not request.user.is_admin:
            return Response({'status': False, 'detail': 'Siz faqat o‘z davomatingizni ko‘ra olasiz!'}, status=403)

        # Studentning davomatlarini olish
        attendances = Attendance.objects.filter(student_id=student_id).order_by("-created_at")

        # Agar hech qanday davomat bo‘lmasa
        if not attendances.exists():
            return Response({'status': False, 'detail': 'Davomat ma’lumotlari topilmadi!'}, status=404)

        # Serializatsiya qilish
        serialized_attendances = AttendanceSerializer(attendances, many=True).data

        # Oy bo‘yicha guruhlash
        grouped_attendances = defaultdict(list)
        for attendance in serialized_attendances:
            created_at = attendance['created_at'][:7]  # YYYY-MM format
            grouped_attendances[created_at].append(attendance)

        # JSON formatda chiqarish
        response_data = [
            {"month": month_name[int(month_year.split("-")[1])],
             "year": month_year.split("-")[0],
             "attendances": records}
            for month_year, records in grouped_attendances.items()
        ]

        # Pagination qo‘llash
        paginator = StudentAttendancePagination()
        paginated_queryset = paginator.paginate_queryset(response_data, request)

        return paginator.get_paginated_response(paginated_queryset)
#Parrent
class ParentViewSet(viewsets.ViewSet):
    permission_classes = [AdminUser]

    def list(self, request):
        parents = Parent.objects.all()
        paginator = Pagination()
        result_page = paginator.paginate_queryset(parents, request)
        serializer = ParentSerializer(result_page, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        parent = get_object_or_404(Parent, pk=pk)
        serializer = ParentSerializer(parent)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], url_path='create/parent')
    @swagger_auto_schema(request_body=ParentSerializer)
    def create_parent(self, request):
        serializer = ParentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'], url_path='update/parent')
    @swagger_auto_schema(request_body=ParentSerializer)
    def update_parent(self, request, pk=None):
        parent = get_object_or_404(Parent, pk=pk)
        serializer = ParentSerializer(parent, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'], url_path='delete/parent')
    def delete_parent(self, request, pk=None):
        parent = get_object_or_404(Parent, pk=pk)
        parent.delete()
        return Response({'status':True,'detail': 'Parent muaffaqiatli uchirildi'}, status=status.HTTP_204_NO_CONTENT)

