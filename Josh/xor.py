# Python 2.7.16 64bit
##################################################################################################################
#  Josh Romero
#  May 8, 2020
#  Introduction to Cybersecurity
##################################################################################################################

import os, sys, operator
from sys import stdout

# name of the file that has the key
filename = "key"

# True if we are in DEBUG mode
DEBUG = False


# Open the key file, convert it to binary the return the results.
def get_key(filename):   
    results = bytearray(open(filename, "rb").read()) 
    return results, len(results)


# Take the input and converts it to binary the returns the results.
def get_plaintext(): 
    plaintxt = raw_input()
    results = bytearray(plaintxt)
    return results, len(results)


# takes the the XOR of ever individual index and stores it in ciphertext at the same index
def _xor():
    ciphertext = bytearray(plaintext_length)
    for j in range(plaintext_length):
        ciphertext[j] = plaintext[j] ^ key[j%key_length]    # XOR's 
        if DEBUG:
            print ciphertext[j]
    return ciphertext


# sends the result to stdout 
def _display():
    if DEBUG:
        sys.stdout.write(key)
        sys.stdout.write("\n")
        sys.stdout.write(plaintext)
        sys.stdout.write("\n")
        sys.stdout.flush()

    sys.stdout.write(ciphertext)
    sys.stdout.write("\n")
    sys.stdout.flush()


###############################################        Main Code         ##############################################



key, key_length = get_key(filename)                # gets the key from the file 
plaintext, plaintext_length = get_plaintext()      # get the plaintext from the input
ciphertext = _xor()                                # gets the XOR of the file and the key
_display()                                         # sends the results to stdout