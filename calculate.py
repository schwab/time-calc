from load_sch import loader
from datetime import date, timedelta
import datetime

l=loader()
l.load_from_file('schedule1.csv')
currentDateTime = datetime.datetime.today()

schItems = []
lastTime = None
secondLastTime = None

for x in l.schedule:
	if x['isSet']:
		schItems.append( (x['dtTime'],x['isSet'], x['start']))



	if x["isSet"] and currentDateTime <= x["dtTime"]:
		if x["start"] == True:
			if lastTime != None:
				if lastTime["start"] == False:
					ts = currentDateTime - secondLastTime["dtTime"]
					print 'false',ts.days * 24 * 3600 + ts.seconds
					break
				else:
					ts = currentDateTime - lastTime["dtTime"]
					print 'true',ts.days * 24 * 3600 + ts.seconds
					break
			else:
				print"ERROR: givin time is before start of week"
	else:			
		if lastTime != None:
			secondLastTime = lastTime
		lastTime = x

	


