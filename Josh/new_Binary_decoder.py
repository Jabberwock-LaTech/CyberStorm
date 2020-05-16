# Python 2.7.16 64bit
from sys import *



def decode(binary, n):
    text = ""
    i = 0
    while i < len(binary):
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


binary = stdin.read().rstrip("\n")

# if len(binary)%7 == 0:
text = decode(binary, 7)
print "7-bit:"
print text
# if len(binary) % 8 == 0:
text = decode(binary, 8)
print "8-bit:"
print text



