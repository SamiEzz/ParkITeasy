
from Availability import *

class Place:
	def __init__(self, id, name, availability, isFree, floor):
		self.id = id
		self.name = name
		self.availability = availability
		self.isFree = isFree
		self.floor = floor
		

	def get_id(self):
		return self.id

	def get_name(self):
		return self.name

	def get_availability(self):
		return self.availability

	def get_isFree(self):
		return self.isFree

	def get_floor(self):
		return self.floor
