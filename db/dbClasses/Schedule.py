from .Essentials import DbPath
from datetime import datetime


def getSchedule():
    return DbPath("rooms").getDb()


def getLibrary():
    return DbPath("library").getDb()


def updateLibrary(val):
    return DbPath("library").writeToDb(val)


class Schedule:
    def getAll():
        db = getSchedule()  # get the  room
        lsts = db["days"]

        lsts2 = []

        for i in range(lsts.__len__()):
            # i is a day
            lsts2.append([])
            for j in range(lsts[i].__len__()):
                # j is an hour content
                lsts2[i].append([])
                for k in range(lsts[i][j].__len__()):
                    # k is a room num
                    lsts2[i][j].append({})
                    lsts2[i][j][k][lsts[i][j][k].__str__()] = True
                    print(lsts[i][j][k])

        for i in range(lsts2.__len__()):
            for j in range(lsts2[i].__len__()):
                print(lsts2[i][j])
                for k in range(100, 200):
                    if not {str(k): True} in lsts2[i][j]:
                        lsts2[i][j].append({str(k): False})

        # updateLibrary(lsts2)

        # show only today's db
        # add free/ occp attributes
        # free after each session

        # return db
        return lsts2

    def getAv():
        db = getSchedule()
        lsts = db["days"]

        lsts2 = []

        for i in range(lsts.__len__()):
            # i is a day
            lsts2.append([])
            for j in range(lsts[i].__len__()):
                # j is an hour content
                lsts2[i].append([])
                for k in range(lsts[i][j].__len__()):
                    if not lsts[i][j][k][list(lsts[i][j][k].keys())[0]]:
                        lsts2[i][j].append({list(lsts[i][j][k].keys())[0]:False})

                    

        return lsts2

# Schedule.getAll()
