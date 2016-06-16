from load_sch import loader
from datetime import date, timedelta
import datetime
import os

class calculate:
	l=None
	defaultFile='schedule1.csv'
	currentDateTime = None 
	last=None
	beforeLast = None
	schItems =[]
	def __init__(self,path=None,date=None):
		self.l = loader()
		if not path:
			path = self.defaultFile
		self.l.load_from_file(path)
		if not date:
			self.currentDateTime = datetime.datetime.today()
		else:
			self.currentDateTime = date
		

	def getItems(self):
		for x in self.l.schedule:
			yield x
			self.beforeLast = self.last
			self.last = x
			
	def calc_schedule_intercept(self):
		schedule_generator =  self.getItems()
		# sorry, apparently iterators and the next keyword don't work in jython
		# adding an old fashion loop instead	
		#current = next(schedule_generator)	
		#while current :
		for current in self.l.schedule:
			if current['isSet']:
				self.schItems.append( (current['dtTime'],current['isSet'], current['start']))
			if current["isSet"] and self.currentDateTime <= current["dtTime"]:
				if current["start"] == True:
					if self.last != None:
						if self.last["start"] == False:
							ts = self.last - self.beforeLast["dtTime"]
							print 'false',ts.days * 24 * 3600 + ts.seconds
							break
						else:
							ts = self.currentDateTime - self.last["dtTime"]
							print 'true',ts.days * 24 * 3600 + ts.seconds
							break
					else:
						print"ERROR: givin time is before start of week"
			else:			
				#current = next(schedule_generator)
				self.beforeLast = self.last
				self.last = current
if __name__ == "__main__":
	c = calculate()
	c.calc_schedule_intercept()

