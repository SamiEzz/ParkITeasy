import json

env = open("env.json", mode='r')
envirJson=json.load(env)

def getKeyFromJson(key):
    return envirJson[key]
    