from datetime import datetime

from django.db.models import Count, Q, Sum
from django.utils.dateparse import parse_datetime
from django.utils.timezone import make_aware
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app_attendance.models import Attendance
from app_common.permissions import AdminUser
from app_courses.models import Group, Course
from app_payments.models import Payment
from app_users.models import Student, Teacher

class StudentFilterView(APIView):
    permission_classes = [AdminUser]
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'start_date', openapi.IN_QUERY,
                description="Filter by start date (format: YYYY-MM-DDTHH:MM:SS)",
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_DATETIME
            ),
            openapi.Parameter(
                'end_date', openapi.IN_QUERY,
                description="Filter by end date (format: YYYY-MM-DDTHH:MM:SS)",
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_DATETIME
            ),
        ]
    )
    def get(self, request):

        start_date = request.GET.get("start_date")  # YYYY-MM-DD
        end_date = request.GET.get("end_date")  # YYYY-MM-DD

        if not start_date or not end_date:
            return Response(
                {"error": "start_date va end_date berilishi shart"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            #  String sanalarni datetime obyektiga aylantiramiz
            start_date = parse_datetime(f"{start_date} 00:00:00")
            end_date = parse_datetime(f"{end_date} 23:59:59")

            # Agar vaqt zonasi yo‘q bo‘lsa, uni UTC ga o‘tkazamiz
            start_date = make_aware(start_date)
            end_date = make_aware(end_date)

        except Exception:
            return Response(
                {"error": "Sana formati noto‘g‘ri. YYYY-MM-DD bo‘lishi kerak."},
                status=status.HTTP_400_BAD_REQUEST
            )
        total_students = Student.objects.all()

        graduated_students = Student.objects.filter(
            group__in=Group.objects.filter(active=False),
            created_at__gte=start_date,
            created_at__lte=end_date
        ).distinct()

        studying_students = Student.objects.filter(
            group__in=Group.objects.filter(active=True),
            created_at__gte=start_date,
            created_at__lte=end_date
        ).distinct()

        registered_students = Student.objects.filter(
            created_at__gte=start_date,
            created_at__lte=end_date
        )
        return Response({
            "total_students": total_students.count(),
            "register_students": registered_students.count(),
            "graduated_students": graduated_students.count(),
            "studying_students": studying_students.count(),
            "date": [start_date, end_date],

        }, status=status.HTTP_200_OK)

class TeacherFilterView(APIView):
    permission_classes = [AdminUser]
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'start_date', openapi.IN_QUERY,
                description="Filter by start date (format: YYYY-MM-DDTHH:MM:SS)",
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_DATETIME
            ),
            openapi.Parameter(
                'end_date', openapi.IN_QUERY,
                description="Filter by end date (format: YYYY-MM-DDTHH:MM:SS)",
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_DATETIME
            ),
        ]
    )
    def get(self, request):

        start_date = request.GET.get("start_date")
        end_date = request.GET.get("end_date")

        if not start_date or not end_date:
            return Response(
                {"error": "start_date va end_date berilishi shart"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            #  String sanalarni datetime obyektiga aylantiramiz
            start_date = parse_datetime(f"{start_date} 00:00:00")
            end_date = parse_datetime(f"{end_date} 23:59:59")

            # Agar vaqt zonasi yo‘q bo‘lsa, uni UTC ga o‘tkazamiz
            start_date = make_aware(start_date)
            end_date = make_aware(end_date)

        except Exception:
            return Response(
                {"error": "Sana formati noto‘g‘ri. YYYY-MM-DD bo‘lishi kerak."},
                status=status.HTTP_400_BAD_REQUEST
            )
        total_teachers = Teacher.objects.all()

        registered_teachers = Teacher.objects.filter(
            created_at__gte=start_date,
            created_at__lte=end_date
        )
        teachers_with_most_students = (
            Student.objects.filter(created_at__gte=start_date, created_at__lte=end_date)
            .values("group__teacher__user__full_name")
            .annotate(total_students=Count("id"))
            .order_by("-total_students")[:10]
        )

        return Response({
            "total_teachers": total_teachers.count(),

            "registered_teachers": registered_teachers.count(),
            "top_teachers": teachers_with_most_students,
            "date": [start_date, end_date],

        }, status=status.HTTP_200_OK)

class GroupFilterView(APIView):
    permission_classes = [AdminUser]
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'start_date', openapi.IN_QUERY,
                description="Filter by start date (format: YYYY-MM-DDTHH:MM:SS)",
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_DATETIME
            ),
            openapi.Parameter(
                'end_date', openapi.IN_QUERY,
                description="Filter by end date (format: YYYY-MM-DDTHH:MM:SS)",
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_DATETIME
            ),
        ]
    )
    def get(self, request):

        start_date = request.GET.get("start_date")
        end_date = request.GET.get("end_date")

        if not start_date or not end_date:
            return Response(
                {"error": "start_date va end_date berilishi shart"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            #  String sanalarni datetime obyektiga aylantiramiz
            start_date = parse_datetime(f"{start_date} 00:00:00")
            end_date = parse_datetime(f"{end_date} 23:59:59")

            # Agar vaqt zonasi yo‘q bo‘lsa, uni UTC ga o‘tkazamiz
            start_date = make_aware(start_date)
            end_date = make_aware(end_date)

        except Exception:
            return Response(
                {"error": "Sana formati noto‘g‘ri. YYYY-MM-DD bo‘lishi kerak."},
                status=status.HTTP_400_BAD_REQUEST
            )
        total_groups = Group.objects.count()
        active_groups = Group.objects.filter(active=True,
        created_at__gte=start_date,created_at__lte=end_date).count()
        inactive_groups = Group.objects.filter(active=False,created_at__gte=start_date,
        created_at__lte=end_date).count()
        registered_groups = Group.objects.filter(created_at__gte=start_date,
        created_at__lte=end_date)

        return Response(
                {
                    "total": total_groups,
                    "active": active_groups,
                    "inactive": inactive_groups,
                    "registered_groups": registered_groups.count(),

                }, status=status.HTTP_200_OK)

class CourseFilterView(APIView):
    permission_classes = [AdminUser]
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'start_date', openapi.IN_QUERY,
                description="Filter by start date (format: YYYY-MM-DDTHH:MM:SS)",
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_DATETIME
            ),
            openapi.Parameter(
                'end_date', openapi.IN_QUERY,
                description="Filter by end date (format: YYYY-MM-DDTHH:MM:SS)",
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_DATETIME
            ),
        ]
    )
    def get(self, request):

        start_date = request.GET.get("start_date")
        end_date = request.GET.get("end_date")

        if not start_date or not end_date:
            return Response({"error": "date1 va date2 berilishi shart"}, status=status.HTTP_400_BAD_REQUEST)

        start_date = parse_datetime(start_date)
        end_date = parse_datetime(end_date)

        # Agar vaqt zonasi yo‘q bo‘lsa, uni UTC ga o‘tkazamiz
        start_date = make_aware(start_date)
        end_date = make_aware(end_date)

        if not start_date or not end_date:
            return Response({"error": "Sana formati noto‘g‘ri. YYYY-MM-DD bo‘lishi kerak."},
                            status=status.HTTP_400_BAD_REQUEST)

        courses_statistics = (
            Course.objects.annotate(
                total_registered_students=Count("c_student",
                                                filter=Q(c_student__created_at__range=[start_date, end_date])),
                total_studying_students=Count("c_student", filter=Q(c_student__group__active=True,
                                                                    c_student__created_at__range=[start_date,
                                                                                                  end_date])),
                total_graduated_students=Count("c_student", filter=Q(c_student__group__active=False,
                                                                     c_student__created_at__range=[start_date,
                                                                                                   end_date]))
            ).values("title", "total_registered_students", "total_studying_students", "total_graduated_students")
        )

        return Response(courses_statistics, status=status.HTTP_200_OK)

class AttendanceFilterView(APIView):
    permission_classes = [AdminUser]
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'start_date', openapi.IN_QUERY,
                description="Filter by start date (format: YYYY-MM-DDTHH:MM:SS)",
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_DATETIME
            ),
            openapi.Parameter(
                'end_date', openapi.IN_QUERY,
                description="Filter by end date (format: YYYY-MM-DDTHH:MM:SS)",
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_DATETIME
            ),
        ]
    )
    def get(self, request):
        start_date = request.GET.get("start_date")
        end_date = request.GET.get("end_date")

        if not start_date or not end_date:
            return Response({"error": "start_date va end_date berilishi shart"}, status=status.HTTP_400_BAD_REQUEST)

        start_date = parse_datetime(start_date)
        end_date = parse_datetime(end_date)

        if not start_date or not end_date:
            return Response({"error": "Sana formati noto‘g‘ri. YYYY-MM-DD bo‘lishi kerak."}, status=status.HTTP_400_BAD_REQUEST)

        attendance_stats = (
            Attendance.objects.filter(created_at__range=[start_date, end_date])
            .aggregate(
                total_present=Count("id", filter=Q(status=1)),  # Keldi
                total_absent=Count("id", filter=Q(status=2)),  # Kelmadi
                total_late=Count("id", filter=Q(status=3)),  # Kechikdi
                total_excused=Count("id", filter=Q(status=4)),  # Sababli
            )
        )

        return Response(attendance_stats, status=status.HTTP_200_OK)


class PaymentFilterView(APIView):
    permission_classes = [AdminUser]
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'start_date', openapi.IN_QUERY,
                description="Filter by start date (format: YYYY-MM-DDTHH:MM:SS)",
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_DATETIME
            ),
            openapi.Parameter(
                'end_date', openapi.IN_QUERY,
                description="Filter by end date (format: YYYY-MM-DDTHH:MM:SS)",
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_DATETIME
            ),
        ]
    )
    def get(self, request):
        start_date = request.GET.get("start_date")
        end_date = request.GET.get("end_date")

        if not start_date or not end_date:
            return Response({"error": "start_date va end_date berilishi shart"}, status=status.HTTP_400_BAD_REQUEST)

        start_date = parse_datetime(start_date)
        end_date = parse_datetime(end_date)

        if not start_date or not end_date:
            return Response({"error": "Sana formati noto‘g‘ri. YYYY-MM-DD bo‘lishi kerak."},
                            status=status.HTTP_400_BAD_REQUEST)

        payment_stats = (
            Payment.objects.filter(created_at__range=[start_date, end_date])
            .aggregate(
                total_amount=Sum("price"),  # Jami to‘langan summa
                total_students=Count("student", distinct=True)  # To‘lov qilgan studentlar soni
            )
        )

        return Response(payment_stats, status=status.HTTP_200_OK)





