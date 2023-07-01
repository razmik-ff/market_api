from django.urls import path, include
from .views import CompanyAPIView, CompanyDetailAPIView


urlpatterns = [
    path('', CompanyAPIView.as_view()),
    path('<uuid:c_pk>', CompanyDetailAPIView.as_view()),
]
