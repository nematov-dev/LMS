from django.urls import path

from app_common.views import InfoTemplateView

app_name = 'infos'
urlpatterns = [
    path('',InfoTemplateView.as_view(),name='info'),
]