import json

from response_handler import errors

"""
Get`s under
"""


def getConfigJson():
    try:
        with open('config.json', 'r') as file:
            return json.loads(file.read())
    except Exception:
        raise FileExistsError(errors.readingConfigJsonFile())


def getSteamAccountUsername():
    try:
        with open('config.json', 'r') as file:
            file_json = json.loads(file.read())
            username = file_json["userdata"]["username"]
            if len(username) <= 0:
                username = 'N/A'
            return username
    except Exception:
        raise FileExistsError(errors.readingConfigJsonFile())


def getSteamAccountPassword():
    try:
        with open('config.json', 'r') as file:
            file_json = json.loads(file.read())
            return file_json["userdata"]["password"]
    except Exception:
        raise FileExistsError(errors.readingConfigJsonFile())


def getNickNamesSet():
    try:
        with open('config.json', 'r') as file:
            file_json = json.loads(file.read())
            nicknames_list = file_json["nickNamesManagement"]["nickNamesForChange"]
            if len(nicknames_list) <= 0:
                nicknames_list = 'N/A'
            return nicknames_list
    except Exception:
        raise FileExistsError(errors.readingConfigJsonFile())


def getAutoChangeTime():
    try:
        with open('config.json', 'r') as file:
            file_json = json.loads(file.read())
            return file_json["autoChangeTime"]
    except Exception:
        raise FileExistsError(errors.readingConfigJsonFile())


"""
Set`s under
"""


def setSteamAccountUsername(username):
    try:
        file_json = getConfigJson()
        file_json["userdata"]["username"] = username
        with open('config.json', 'w') as file:
            file.write(json.dumps(file_json, indent=4))
    except Exception:
        raise FileExistsError(errors.writingConfigJsonFile())


def setSteamAccountPassword(password):
    try:
        file_json = getConfigJson()
        file_json["userdata"]["password"] = password
        with open('config.json', 'w') as file:
            file.write(json.dumps(file_json, indent=4))
    except Exception:
        raise FileExistsError(errors.writingConfigJsonFile())


"""
Check`s under
"""


def checkSteamAccountUsername():
    try:
        file_json = getConfigJson()
        if len(file_json["userdata"]["username"]) <= 3:
            return False
        return True
    except Exception:
        raise FileExistsError(errors.readingConfigJsonFile())


def checkSteamAccountPassword():
    try:
        file_json = getConfigJson()
        if len(file_json["userdata"]["password"]) <= 3:
            return False
        return True
    except Exception:
        raise FileExistsError(errors.readingConfigJsonFile())


def checkNicknamesSetEmpty():
    try:
        file_json = getConfigJson()
        if not len(file_json["nickNamesManagement"]["nickNamesForChange"]) <= 2:
            return False
        return True
    except Exception:
        raise FileExistsError(errors.readingConfigJsonFile())
