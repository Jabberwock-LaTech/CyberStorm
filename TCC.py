# Names:        James R. Henry
# Date:         04/24/2020
# Assignment:   Chat (Timing) Covert Channel
# Version:      Python 2

import socket
from time import time
from sys import stdout
from binascii import unhexlify


# enables debugging output
DEBUG = False

# set the server's IP address and port
ip = "138.47.99.163"
port = 12321

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))

# store the received bits in binary
covert_bin = ""

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
    # if delta is greater than .1
    if (0.225 >= delta >= 0.175):
        # record a 1
        covert_bin += "1"
    # otherwise
    elif(0.075 <= delta <= 0.125):
        # store a 0
        covert_bin += "0"
    if (DEBUG):
		stdout.write(" {}\n".format(delta))
		stdout.flush()

# close the connection to the server
s.close()

# received covert messsage
covert = ""

# counter to step through covert_bin
i = 0

# step through the binary
while (i < len(covert_bin)):
    # process one byte at a time
    b = covert_bin[i:i + 8]
    # convert it to ASCII
    n = int("0b{}".format(b), 2)
    try:
        # convert ASCII to alpha
        covert += unhexlify("{0:x}".format(n))
    # exception catch
    except TypeError:
        # add a ? if bad ASCII
        covert += "?"
    # increment the counter to the next character in binary
    i += 8

# print the hidden message
print "\n"
print covert