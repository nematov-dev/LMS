from django.contrib import admin

from app_payments.models import Payment, PaymentType, Month

admin.site.register([Payment,PaymentType,Month])
