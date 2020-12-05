import requests
from secretAccess import *
from point import *


def getLonLatFromAdress(adresse):
    access_key = getAccessKey()
    getAdresse = "http://api.positionstack.com/v1/forward?access_key="+access_key+"&query="
    response = requests.get(getAdresse+adresse)
    response_dict = json.loads(response.text)
    lon = float(response_dict["data"][0]["longitude"])
    lat = float(response_dict["data"][0]["latitude"])
    p = Point(lon,lat)
    return p
