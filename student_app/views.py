from django.shortcuts import render
from auth_app.views import Student as StudentAuth
# Create your views here.


@StudentAuth.check_login
def student_app(request):
    return render(request, "student_app/student_app.html", {})