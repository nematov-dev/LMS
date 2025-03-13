from datetime import datetime

from django.db.models import Count, Q, Sum
from django.utils.timezone import make_aware
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser

from app_attendance.models import Attendance
from app_courses.models import Group, Course
from app_payments.models import Payment
from app_users.models import Student, Teacher
from app_statistics.serializers import DateFilterSerializer


class StudentFilterView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(request_body=DateFilterSerializer)
    def post(self, request):
        serializer = DateFilterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        start_date = serializer.validated_data['start_date']
        end_date = serializer.validated_data['end_date']

        start_date = make_aware(datetime.combine(start_date, datetime.min.time()))
        end_date = make_aware(datetime.combine(end_date, datetime.max.time()))

        total_students = Student.objects.count()
        graduated_students = Student.objects.filter(group__active=False, created_at__range=[start_date, end_date]).count()
        studying_students = Student.objects.filter(group__active=True, created_at__range=[start_date, end_date]).count()
        registered_students = Student.objects.filter(created_at__range=[start_date, end_date]).count()

        return Response({
            "total_students": total_students,
            "registered_students": registered_students,
            "studying_students": studying_students,
            "graduated_students": graduated_students,
        }, status=status.HTTP_200_OK)


class TeacherFilterView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(request_body=DateFilterSerializer)
    def post(self, request):
        serializer = DateFilterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        start_date = serializer.validated_data['start_date']
        end_date = serializer.validated_data['end_date']

        start_date = make_aware(datetime.combine(start_date, datetime.min.time()))
        end_date = make_aware(datetime.combine(end_date, datetime.max.time()))

        total_teachers = Teacher.objects.count()
        registered_teachers = Teacher.objects.filter(created_at__range=[start_date, end_date]).count()

        top_teachers = (
            Student.objects.filter(created_at__range=[start_date, end_date])
            .values("group__teacher__user__full_name")
            .annotate(total_students=Count("id"))
            .order_by("-total_students")[:10]
        )

        return Response({

            "total_teachers": total_teachers,
            "registered_teachers": registered_teachers,
            "top_teachers": top_teachers,

        }, status=status.HTTP_200_OK)


class GroupFilterView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(request_body=DateFilterSerializer)
    def post(self, request):
        serializer = DateFilterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        start_date = serializer.validated_data['start_date']
        end_date = serializer.validated_data['end_date']

        start_date = make_aware(datetime.combine(start_date, datetime.min.time()))
        end_date = make_aware(datetime.combine(end_date, datetime.max.time()))

        total_groups = Group.objects.count()
        active_groups = Group.objects.filter(active=True, created_at__range=[start_date, end_date]).count()
        inactive_groups = Group.objects.filter(active=False, created_at__range=[start_date, end_date]).count()
        registered_groups = Group.objects.filter(created_at__range=[start_date, end_date]).count()

        return Response({
            "total": total_groups,
            "active": active_groups,
            "inactive": inactive_groups,
            "registered_groups": registered_groups,
        }, status=status.HTTP_200_OK)


class CourseFilterView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(request_body=DateFilterSerializer)
    def post(self, request):
        serializer = DateFilterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        start_date = serializer.validated_data['start_date']
        end_date = serializer.validated_data['end_date']

        start_date = make_aware(datetime.combine(start_date, datetime.min.time()))
        end_date = make_aware(datetime.combine(end_date, datetime.max.time()))

        courses_statistics = (
            Course.objects.annotate(
                total_registered_students=Count("c_student", filter=Q(c_student__created_at__range=[start_date, end_date])),
                total_studying_students=Count("c_student", filter=Q(c_student__group__active=True, c_student__created_at__range=[start_date, end_date])),
                total_graduated_students=Count("c_student", filter=Q(c_student__group__active=False, c_student__created_at__range=[start_date, end_date]))
            ).values("title", "total_registered_students", "total_studying_students", "total_graduated_students")
        )
        return Response(courses_statistics, status=status.HTTP_200_OK)


class AttendanceFilterView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(request_body=DateFilterSerializer)
    def post(self, request):
        serializer = DateFilterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        start_date = serializer.validated_data['start_date']
        end_date = serializer.validated_data['end_date']

        start_date = make_aware(datetime.combine(start_date, datetime.min.time()))
        end_date = make_aware(datetime.combine(end_date, datetime.max.time()))

        attendance_stats = (
            Attendance.objects.filter(created_at__range=[start_date, end_date])
            .aggregate(
                total_present=Count("id", filter=Q(status=1)),
                total_absent=Count("id", filter=Q(status=2)),
                total_late=Count("id", filter=Q(status=3)),
                total_excused=Count("id", filter=Q(status=4)),
            )
        )
        return Response(attendance_stats, status=status.HTTP_200_OK)


class PaymentFilterView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(request_body=DateFilterSerializer)
    def post(self, request):
        serializer = DateFilterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        start_date = serializer.validated_data['start_date']
        end_date = serializer.validated_data['end_date']

        start_date = make_aware(datetime.combine(start_date, datetime.min.time()))
        end_date = make_aware(datetime.combine(end_date, datetime.max.time()))

        payment_stats = (
            Payment.objects.filter(created_at__range=[start_date, end_date])
            .aggregate(
                total_amount=Sum("price"),
                total_students=Count("student",distinct=True)
            )
        )
        return Response(payment_stats, status=status.HTTP_200_OK)
