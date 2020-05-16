# Python 2.7.16 64bit
##################################################################################################################
#  Josh Romero
#  April 3, 2020
#  Introduction to Cybersecurity
##################################################################################################################

# NOTE:::::::::::::::   YOU MUST CHANGE THE IP ADDRESS AND PORT NUMBER TO THE APPROPRIATE ONE FOR YOUR SYSTEM

from ftplib import FTP
from sys import *


# # The FTP method
Method = 10

# globals (FTP specifics)
IP = "jeangourd.com"            ##############      CHANGE THIS TO CORRECT IP ADDRSS
PORT = 8008                       ##############      CHANGE THIS TO CORRECT PORT NUMBER
FOLDER = "/.secretstorage/.folder2/.howaboutonemore/"                   ##############      CHANKGE THIS TO CORRECT FOLDER

# The file/folder contects
contents = []

# Connect to the FTP server on the specified IP address and port, navagate to the specified folder, fetch a file listing, and disconnect 
ftp = FTP()
ftp.connect(IP, PORT)       # opens the connection at the specified IP address and port number
ftp.login("valkyrie", "chooseroftheslain")                 # logs in as anonymous with the "" password
ftp.cwd(FOLDER)             # changes to the advised directory
ftp.dir(contents.append)    # appends the list information in the advised directory to the contents string
ftp.quit()                  # closes the connection


# Deccodes the binary results of the file translation
def decode(binary, n):
    text = ""
    i = 0
    while (i < len(binary)):
        byte = binary[i:i+n]
        byte = int(byte, 2)
        if byte == 8:
            text = text[:-1]
        elif byte == 9:
            text += "   "
        else:
            text += chr(byte)
        i += n
    return text


# Displays the files listing

def converter(binary, method):
    # ###################### Changed this ##############################
    # contents = [1000]
    # contents = stdin.read().rstrip("\n").split("\n")
    # ###################### Changed this ##############################

    
    for row in contents:
        if method == 7:
            if row[:3] == '---':        # if "___" at the begining of the file information then it is par of the code 
                for index in row[3:10]: # goes thru each one and if it is a "-", add 0, else add 1
                    if index == "-":
                        binary += "0"
                    else:
                        binary += "1"
        if method == 10:
            for index in row[:10]:
                if index == "-":
                    binary += "0"
                else:
                    binary += "1"

    return binary



#########################################       Main Code       ##########################################################


binary = ""

if len(binary) % 7 == 0 or len(binary) % 10 == 0:
    binary = converter(binary, Method)
    text = decode(binary, Method)
    if Method == 7:
        print "7-bit:"
    if Method == 10:
        print "10-bit"
    print text

