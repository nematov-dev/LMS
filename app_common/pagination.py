from collections import defaultdict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class Pagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 50


class StudentAttendancePagination(PageNumberPagination):
    page_size = 1  # Har bir oy uchun maksimal yozuvlar soni
    page_size_query_param = 'page_size'
    max_page_size = 50