##############################################
# Jace Ziegler
# 5/5/2020
# simplified idea, makes a code based on what time it is
# use Python 3
#################################################
from sys import stdin
from datetime import datetime
from hashlib import md5
import pytz

#############################################################################################################
def hashMd5(data):
    encode = data.encode()
    hash1 = md5(encode)
    final = hash1.hexdigest()
    return final

def convertToUtc(dt):
    native = datetime.strptime(dt, "%Y %m %d %H %M %S")
    timezone = pytz.timezone("America/Chicago")
    makeLocal = timezone.localize(native, is_dst=None)
    dtUtc = makeLocal.astimezone(pytz.utc)
    return dtUtc

################################################################################################

#dubug mode?
DEBUG = False

#set to True if on the callenge server
ON_SERVER = False

#Valid time interval in sec
INTERVAL = 60

#manual current datetime? change to empty to get currenttime
MANUAL_DATETIME = ""
#MANUAL_DATETIME = ""

#Manual_datetime is not set get cur datetime
if(MANUAL_DATETIME == ""):
    currentTime = datetime.now().strftime("%Y %m %d %H %M %S")
    currentTime = convertToUtc(currentTime)
else:
    currentTime = convertToUtc(MANUAL_DATETIME)
    
#Recive epoch
epoch = stdin.read().rstrip("\n")
l = ""
for x in range(1,3):
    l += epoch[-x]
    l = l[::-1]
epoch = convertToUtc(epoch)

if(DEBUG):
    print("Current (UTC): {}".format(currentTime))
    print("Epoch (UTC): {}".format(epoch))

#get time ellapsed
ellapsed = (currentTime - epoch).total_seconds()

if(DEBUG):
    print("Seconds: {}".format(ellapsed))

#back up to current 60 sec interval
cdstr = str(currentTime)

c = ""
for x in range(7,9):
    c += cdstr[-x]
c = c[::-1]
c = int(c)
l = int(l)
if(c < l):
    time = ((l-c)*-1)-2
else:
    time = (l-c)
sec = (int((currentTime-epoch).total_seconds())+time)
ellapsed = str(sec)
if(DEBUG):
    print("Seconds: {}".format(ellapsed))

#hash twice
ellapsed = hashMd5(str(int(ellapsed)))
if(DEBUG):
    print("MD5 #1: {}".format(ellapsed))

ellapsed = hashMd5(ellapsed)
if(DEBUG):
    print("MD5 #2: {}".format(ellapsed))

#left to right first two letters
code = ""
i = 0
while(len(code) < 2):
    if (ellapsed[i].isalpha()):
        code += ellapsed[i]
    i+=1

#right to left first two digits
i = len(ellapsed)-1
while(len(code) < 4):
    if (ellapsed[i].isdigit()):
        code += ellapsed[i]
    i-=1

#print out the code
print("Code: {}".format(code))


    
    
