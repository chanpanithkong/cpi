from datetime import datetime
import logging

class userlogging:
    
    def __init__(self,clientid=None, message=None):
        self.clientid = clientid
        self.message = message
    
    def degbuglog(clientid, url, message):
        msg = clientid + ' : ' + url + ' : ' + message
        now = datetime.now()
        logdate = now.strftime("%Y-%m-%d")
        logfilename = 'logging/access_'+logdate+".log"
        format = '%(asctime)s : %(levelname)s : %(name)s : %(message)s'
        logging.basicConfig(filename=logfilename, level=logging.DEBUG, format=format)
        logging.debug(msg)
