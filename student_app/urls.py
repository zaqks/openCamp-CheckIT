from django.urls import path
from .views import student_app

urlpatterns = [
    path("", student_app)
]
