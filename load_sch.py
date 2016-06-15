import csv
import os 
import time
import datetime
from datetime import date, timedelta

class loader:
	today = 0
	schedule=[]
	def __init__(self):
		self.today = datetime.datetime.today()
		self.weekday = self.today.weekday()
		self.day1 = self.today- timedelta(days=self.weekday)
	def load_from_file(self,path):
		#print("load file " + path )
		if not os.path.exists(path):
			print('File not found ' + path)			
		else:
			#print("Loading " + path)
			try:
				f = open(path,'rb')
				reader = csv.reader(f)
				doy = 0
				working = 0
				for row in reader:
					working = True
					doy = doy+1
					ptr = 0
					for schedIndex in range(15):
						t = []
						for timeIndex in range(3):
							t.append(int(row[ptr]))
							ptr += 1		
						self.create_sch_entry(doy,tuple(t),working)
						working = not working	
					#print row
			finally:
				f.close()	
	def create_sch_entry(self,doy,t,startstop):
		doyDate = self.day1 + timedelta(days = doy-1)
		sch = {'isSet':True,'dtTime':0,'start':startstop}
		if t[0] == 24:
			sch['isSet']=False
		else:
			sch['dtTime'] = doyDate.replace(hour=t[0],minute=t[1],second=t[2])
		self.schedule.append(sch)
		#entry = {'time':								

if __name__ == '__main__':
	l = loader()
	l.load_from_file('schedule1.csv')
	for x in l.schedule:
		print x
