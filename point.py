from math import *

class Point:
    def __init__(self, lon, lat,isValid=0):
        self.isValid=isValid
        self.lon = lon
        self.lat = lat 
    def setInvalid(self):
        self.isValid=0
    def setValid(self):
        self.isValid==1
    