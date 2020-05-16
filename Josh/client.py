# Python 2.7.16 64bit
##################################################################################################################
#  Josh Romero
#  April 3, 2020
#  Introduction to Cybersecurity
##################################################################################################################

import socket
from sys import stdout
from time import time
from binascii import *


# decodes the encoded message and saves it to covert
def decode_message(covert_bin):
	i = 0
	covert = ""
	while (i < len(covert_bin)):
		# process one byte at a time
		b = covert_bin[i:i + 8]
		# convert it to ASCII
		n = int("0b{}".format(b), 2)
		try:
			covert += unhexlify("{0:x}".format(n))
			if covert[-3:] == "EOF":
				break
		except TypeError:
			covert += "?"
		# stop at the string "EOF"
		i += 8
	return covert


# gets data from the server
def get_message(DEBUG):
	# receive data until EOF
	data = s.recv(4096)
	covert_bin = ""
	covert_bin2 = ""
	A = []
	B = []
	time_between = []

	# retreives the data and measures the delay to determine if it is a 1 or 0
	while (data.rstrip("\n") != "EOF"):
		# output the data
		stdout.write(data)
		stdout.flush()
		# start the "timer", get more data, and end the "timer"
		t0 = time()
		data = s.recv(4096)
		t1 = time()
		# calculate the time delta (and output if debugging)
		delta = round(t1 - t0, 3)
		
	################################################			Added this for the Challenge
		time_between.append(delta)


	avg1 = sum(time_between)/len(time_between)

	if DEBUG:
		print avg1		# This will work as long as the time difference between transmissions 
		print t			# does not go lower than .0075, which i dont think it will.
		print m			# lower then .0075 the messages begin to not come out clear
	ONE = avg1	
	###############################################

	for times in time_between:	
		if (times >= ONE):
			covert_bin += "1"
			covert_bin2 += "0"
		else:
			covert_bin += "0"
			covert_bin2 += "1"

		if (DEBUG):
			stdout.write(" {}\n".format(times))
			stdout.flush()

	# close the connection to the server
	s.close()
	return covert_bin, covert_bin2

# puts the covert messages on the screen
def display_message(covert, covert2):
	print "\nMessage: ", covert[:-3], "\n  or \n", "Message: ", covert2[:-3]


##############################################		MAIN CODE		#################################################
# enables debugging output
DEBUG = False

# set the server's IP address and port
ip = "138.47.99.163"
port = 12321

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))



#get the message from server
covert_bin, covert_bin2 = get_message(DEBUG)

# decode the message from server
covert = decode_message(covert_bin)
covert2 = decode_message(covert_bin2)

# send the decoded message to the stdout
display_message(covert, covert2)


