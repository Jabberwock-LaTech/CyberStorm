# Python 2.7.16 64bit
##################################################################################################################
#  Josh Romero
#  May 8, 2020
#  Introduction to Cybersecurity
##################################################################################################################

from datetime import *
from time import *
import pytz
from hashlib import md5


############################################     Variables that can be changed      ##############################
# debug mode
DEBUG = True
# set to True if your on the challenge server
ON_SERVER = False 
# pick the time interval you want to use
INTERVAL = 60
# Timezone
_TIMEZONE = 'US/Central'
# Format for dates and times
FMT = "%Y-%m-%d %H:%M:%S"
##################################################################################################################

# DATETIME - epoch
if DEBUG:
    DATETIME = b"2017 03 23 18 02 06"
else:
    DATETIME = datetime.now(pytz.utc)
epoch = raw_input()


# takes in my hash and get my passphrase
def get_phrase(hashed2):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    nums = '0123456789'
    phrase = ""
    count = 0
    for char in hashed2:                        # Finds the first 2 letters in the hash from front to back
        if count == 2:                          # If 2 has been found get out the loop
            break
        if char in alphabet:   
            phrase += char
            count += 1
    count = 0
    for num in range(len(hashed2) - 1, 0, -1):  # Finds the first 2 numbers in the hash from back to front
        if count == 2:                          # If 2 has been found get out the loop
            break
        if hashed2[num] in nums:
            phrase += hashed2[num]
            count += 1
    phrase += hashed2[(len(hashed2) / 2) - 1]
    return phrase                               # return the passphrase


# formates the current datetime correctly and returns the utc datetime
def get_current(DATETIME):
    # # manually enter the data and time
    local_time = pytz.timezone(_TIMEZONE)
    A = DATETIME.split(" ")
    tmp = ("" + A[0] + "-" + A[1] + "-" + A[2] + " " + A[3] + ":" + A[4] + ":" + A[5])
    naive_datetime = datetime.strptime (tmp, FMT)
    local_datetime = local_time.localize(naive_datetime, is_dst=None)
    utc_datetime = local_datetime.astimezone(pytz.utc)
    return utc_datetime


# formates the epoch datetime correctly and returns the utc datetime
def get_epoch(epoch):
    local_time = pytz.timezone(_TIMEZONE)
    A = epoch.split(" ")
    utc_dt = datetime(int(A[0]), int(A[1]), int(A[2]), int(A[3]), int(A[4]), int(A[5]), tzinfo=pytz.utc)
    tmp = ("" + A[0] + "-" + A[1] + "-" + A[2] + " " + A[3] + ":" + A[4] + ":" + A[5])
    naive_datetime = datetime.strptime (tmp, FMT)
    local_datetime = local_time.localize(naive_datetime, is_dst=None)
    utc_datetime = local_datetime.astimezone(pytz.utc)
    return utc_datetime


######################################      Main Code       ######################################################

# get the utc of the current time
if DEBUG:
    utc_datetime = get_current(DATETIME)
else:
    utc_datetime = DATETIME
# get the utc of the epoch
epoch = get_epoch(epoch)



# determine the time between the Datetime and epoch in seconds
time_between = utc_datetime - epoch
time_between_s = int(time_between.total_seconds())
Main_time_between = str(int(time_between_s / INTERVAL) * INTERVAL)

# get the double md5 hash
hashed = md5(Main_time_between.encode()).hexdigest()
hashed2 = md5(hashed.encode()).hexdigest()

# get the passphrase
phrase = get_phrase(hashed2)

# in DEBUG mode print like this
if DEBUG:
    print "Current (UTC): ", utc_datetime
    print "Epoch (UTC): ", utc_datetime
    print "Seconds: ", time_between_s
    print "Seconds: ", Main_time_between
    print "MD5 #1: ", hashed
    print "MD5 #2: ", hashed2
    print len(hashed2)/2
    print "Code: ", phrase
# Not in DEBUG mode print like this
else:
    print phrase