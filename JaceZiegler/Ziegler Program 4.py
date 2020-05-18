##############################
# Jace Ziegler
# Program 4
# CYEN 301-01
# Program to time how long between charters sent and make that into a message.
###############################

import socket
from sys import stdout
from time import time
from binascii import unhexlify

# enables debugging output
DEBUG = False

#covert binary to be recived
covert_bin = ""

#length of time to determine a one
ONE = 0.1

# set the server's IP address and port
ip = "localhost"
port = 1337

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))

# receive data until EOF
data = s.recv(4096)
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
	#determine wether the timing means zero or one and add it to the binary
	if( delta >= ONE):
                covert_bin += "1"
        else:
                covert_bin += "0"
	if (DEBUG):
		stdout.write(" {}\n".format(delta))
		stdout.flush()

# close the connection to the server
s.close()

#decode the the covert binary
covert = ""
i = 0
while(i < len(covert_bin)):
        # process one byte at a time
        b = covert_bin[i:i + 8]
        # convert it to ASCII
        n = int("0b{}".format(b), 2)
        try:
                covert += unhexlify("{0:x}".format(n))
        except TypeError:
                covert += "?"
        # stop at the string "EOF"
        i+=8
        
#print it out
stdout.write('\nHidden message: "{}"\n'.format(covert))
stdout.flush()

