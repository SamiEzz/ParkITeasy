import json


def getAccessKey():
    env = open("env.json", mode='r')
    envirJson=json.load(env)
    return envirJson["accessKey_positionstack"]
    