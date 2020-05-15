# Names:        James R. Henry
# Date:         03/30/2020
# Assignment:   Binary Decoder
# Version:      Python 2

# import stdin from sys

from sys import stdin

# decode binary string to char string
# binary is the binary string input
# n is the bit length of the ASCII (7 or 8)
def decode(binary, n):
    # string variable to store the chars
    text = ""
    # counter
    i = 0
    # while counter is less than length of binary string
    while (i < len(binary)):
        # store the binary ASCII in byte
        byte = binary[i:i+n]
        # convert the binary to integer
        byte = int(byte, 2)
        # if byte is integer 8
        if (byte == 8):
            # remove the last char of the string
            text = text[:-1]
        # else
        else:
            # convert the integer to char and add to string
            text += chr(byte)
        # increment the counter by the bit length
        i += n
    # return the string
    return text

# pull the binary in, strip the new line, and store in binary
binary = stdin.read().rstrip("\n")

# if the input is 7-bit characters
if (len(binary) % 7 == 0):
    # decode the input with n = 7
    text = decode(binary, 7)
    # print decoded text
    print text
# if the input is 9-bit characters
if (len(binary) % 8 == 0):
    # decode the input with n = 8
    text = decode(binary, 8)
    # print decoded text
    print text
