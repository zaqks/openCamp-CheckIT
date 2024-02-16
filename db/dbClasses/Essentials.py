import orjson
from pathlib import Path
from os.path import exists as fileExists

currentDir = Path(__file__).resolve().parent.parent.parent
currentPath = f"{currentDir}/"
currentDbPath = f"{currentPath}db/"


def openJson(path):
    content = {}
    with open(path, "rb") as f:
        content = orjson.loads(f.read())
        f.close()
    return content


def writeToJson(path, wut):
    with open(path, "wb") as f:
        f.write(orjson.dumps(wut))
        f.close()


dbPaths = {
    "students": "private/students/students.json",
    #
    "rooms": "public/rooms/rooms.json",
    "library": "public/rooms/library.json",
    #
    "rooms3": "public/rooms/rooms3.json",
}


class DbPath:
    def __init__(self, dbName):
        self.dbName = dbName
        self.dbPaths = dbPaths

    def getDbPath(self):
        return f"{currentDbPath}storage/{self.dbPaths[self.dbName]}"

    def getDb(self):
        path = self.getDbPath()
        return openJson(path)

    def writeToDb(self, dbContent):
        path = self.getDbPath()
        writeToJson(path, dbContent)


class StrFilter:
    def __init__(self, word):
        self.word = word

    def nameCheck(self):
        if (
            not self.word.isspace()
            and self.word.__len__() >= 3
            and not ("#" in self.word)
        ):
            return True
        return False

    def posStrNum(self):
        wrd = str(self.word)

        if not wrd.isnumeric():
            return 0

        num = float(wrd)

        if num < 0:
            return 0

        return num

    def pwdCheck(self):
        # not blank + does not contain spaces + len >= 8

        if (
            self.word.isspace()
            or self.word.__contains__(" ")
            or self.word.__len__() < 8
        ):
            return False
        return True

    def phonenumCheck(self):
        word = self.word

        if not word.__contains__(" ") and word.__len__() == 10 and word.isnumeric():
            if word[0] == "0" and word[1] != "9":
                return True

        return False


def reverseDict(oldDict):
    newDict = {}

    oldKeys = list(oldDict.keys())
    oldKeysLen = oldKeys.__len__()

    for i in range(oldKeysLen):
        key = oldKeys[oldKeysLen - i - 1]
        newDict[key] = oldDict[key]

    return newDict
