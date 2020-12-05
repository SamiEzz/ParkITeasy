import json

class Parking:
	def __init__(self, id,adresse, point="", nbPlaces=0,nbFreePlaces=0,isFree=1, timeWindow="",imgUrl=""):
		self.id = id
		self.nbPlaces = nbPlaces
		self.nbFreePlaces = nbFreePlaces		
		self.adresse = adresse
		self.point = point
		self.isFree = isFree
		self.timeWindow = timeWindow
		self.imgUrl = imgUrl
		
	def get_adresse(self):
		return self.adresse

	def get_point(self):
		return self.point

	def get_isFree(self):
		return self.isFree

	def get_timeWindow(self):
		return self.timeWindow

def getParkingsHdr():
	parkingsHdr = []
	parkFile = open("./data/parkings.json", mode='r')
	parkings = json.load(parkFile)
	for parking in parkings:
		parsedParking = Parking(parking["id"],parking["adresse"])
		parkingsHdr.append(parsedParking)
	return parkingsHdr
