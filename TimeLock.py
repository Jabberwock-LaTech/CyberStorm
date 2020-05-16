# Names:        James R. Henry
# Date:         05/08/2020
# Assignment:   TimeLock
# Version:      Python 2

from sys import stdin
from datetime import datetime
import pytz
from hashlib import md5

# debug mode?
DEBUG = False

# on challenge server?
ON_SERVER = False

# Time interval
INTERVAL = 60

# set manual datetime
MANUAL_DATETIME = "2020 05 15 18 42 00"

utc = pytz.UTC
local = pytz.timezone('US/Central')
fmt = "%Y %m %d %H %M %S"

# current time
def currentTime():
    # if manual time has not been sent
    if (MANUAL_DATETIME == ""):
        # get time now and save to current
        current = datetime.now()
        # format time to string removing milliseconds
        current = datetime.strftime(current, fmt)
        # format time from string back to datetime obj
        current = datetime.strptime(current, fmt)
        # add timezone
        current = local.localize(current)
        # convert to UTC
        current = current.astimezone(utc)
        # return current time in UTC
        return current
    # time set manually
    else:
        # convert time string to datetime obj
        current = datetime.strptime(MANUAL_DATETIME, fmt)
        # add timezone
        current = local.localize(current)
        # convert to utc
        current = current.astimezone(utc)
        # return set time in UTC
        return  current

# if on the server get time from server
if (ON_SERVER):
    pass
# else get time from stdin
else:
    # get "epoch" time from console in
    epoch = stdin.read().rstrip("\n")
    # convert epoch time string to datetime obj
    epoch = datetime.strptime(epoch, fmt)
    # add timezone
    epoch = local.localize(epoch)
    # convert to UTC
    epoch = epoch.astimezone(utc)

# get current time
current = currentTime()

# get difference between epoch and current time
delta = current - epoch
# convert difference to seconds
deltaSeconds = delta.seconds + delta.days * 86400

# back up to last minute
back = deltaSeconds % INTERVAL
validTime = deltaSeconds - back

# hash the time
h1 = md5(str(validTime))

# hash it again
h2 = md5(h1.hexdigest())

# counter
i = 0
# final code variable
code = ""

# step through the hash
for char in h2.hexdigest():
    # find the first to letters
    if (char.isalpha() & (i < 2)):
        # add them to the code
        code += char
        # increment the counter
        i += 1

# reset the counter
i = 0
# reverse the hash
h2R = h2.hexdigest()[32::-1]

# step through the reversed hash
for char in h2R:
    # find the first 2 digits
    if (char.isdigit() & (i < 2)):
        # add them to the code
        code += char
        # increment counter
        i += 1

#code += h2R[(len(h2R)/2)-1]
#code += h2R[(len(h2R)/2)]
# print each step's result if debugging
if (DEBUG):
    print("Current (UTC):  "), 
    print(current)
    print("Epoch (UTC):  "),
    print(epoch)
    print("Seconds:  "),
    print(deltaSeconds)
    print("Seconds:  "),
    print(validTime)
    print("MD5 #1:  "),
    print(h1.hexdigest())
    print("MD5 #2:  "),
    print(h2.hexdigest())
    print("Code:  "),
    print(code)
# else print the code
else:
    print "cyberstorm" + code + h2R[((len(h2R)/2)-1)] + h2R[(len(h2R)/2)]
    print "cyberstorm" + code + h2R[(len(h2R)/2)] + h2R[((len(h2R)/2)+1)]
