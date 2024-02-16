from django.http import HttpResponseRedirect
from django.shortcuts import render
from db.dbLinker import Student as StudentDB


class Student:
    def check_login(func):
        def wrapper(request, *args, **kwargs):

            cookies = request.COOKIES
            if cookies.__contains__("username") and cookies.__contains__("password"):
                username = cookies["username"]
                password = cookies["password"]

                # check the id
                # success, mssg = Customer(username).checkPwd(password)
                success = StudentDB(username).auth(password)

                if success:
                    return func(request, **kwargs)

            # delete the current info & redirect to login
            response = HttpResponseRedirect("/")
            response.delete_cookie(
                key="username", path="app")
            response.delete_cookie(
                key="password", path="app")

            return response

        return wrapper


def auth(request):
    if request.method == "POST":
        rqst = request.POST

        valid = True
        vals = {"username": "", "password": ""}

        for i in vals:
            if not i in rqst:
                valid = False
                break

            vals[i] = rqst[i]

        if valid:
            if StudentDB(vals["username"]).auth(vals["password"]):
                response = HttpResponseRedirect("app")

                for i in vals:
                    response.set_cookie(i, vals[i])

                return response

    return render(request, "auth_app/auth_app.html", {})
