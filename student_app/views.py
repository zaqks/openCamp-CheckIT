from django.shortcuts import render
from auth_app.views import Student as StudentAuth
from db.dbLinker import getLibrary, getSchedule, Schedule, Student
# Create your views here.


@StudentAuth.check_login
def student_app(request):
    userId = request.COOKIES["username"]
    user = Student(userId)
    
    username = user.get()[1]["name"]

    return render(request, "student_app/student_app.html", {"library": getLibrary(),
                                                            "avRooms": Schedule.getAv(),
                                                            "allRooms": getSchedule(),
                                                            #
                                                            "username":username
                                                            }
                  )
