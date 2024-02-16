from .Essentials import DbPath


def getStudents():
    return DbPath("students").getDb()


def updateStudents(val):
    DbPath("students").writeToDb(val)


class Student:
    def __init__(self, id):
        self.id = id

    def exists(self):
        users = getStudents()
        return self.id in users

    def get(self):
        if self.exists():
            return [True, getStudents()[self.id]]

        return [False, {}]

    def auth(self, pwd):
        if self.exists():
            return self.get()[1]["password"] == pwd

        return False
