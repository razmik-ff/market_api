from django.urls import path, include
from .views import CompanyAPIView


urlpatterns = [
    path('', CompanyAPIView.as_view()),
]
