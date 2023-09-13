import time
from datetime import datetime

class convertdate:
    
    def convertotimestamp():

        now = datetime.now()
        currentdatetime = now.strftime("%Y-%m-%d %H:%M:%S")
        element = datetime.strptime(currentdatetime,"%Y-%m-%d %H:%M:%S")
        tuple = element.timetuple()
        timestamp = time.mktime(tuple)

        return timestamp
    

