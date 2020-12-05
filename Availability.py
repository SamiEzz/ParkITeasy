class Availability:
	def __init__(self, timeFrame, isFree, weekDays, reservationsList):
		self.timeFrame = timeFrame
		self.isFree = isFree
		self.weekDays = weekDays
		self.reservationsList = reservationsList
		
	def get_timeFrame(self):
		return self.timeFrame

	def get_isFree(self):
		return self.isFree

	def get_weekDays(self):
		return self.weekDays

	def get_reservationsList(self):
		return self.reservationsList


	def __str__():
 		return "timeFrame: " + timeFrame + " , " + "isFree: " + isFree + " , " + "weekDays: " + weekDays + " , " + "reservationsList: " + reservationsList
