################################
# Jace Ziegler
# 5/7/2020
# Python 3
################################
import sys

#name of file to take from
key_file = "key2"

#take key from file
file = open(key_file, "r+b")
key = file.read()
file.close()
key = bytearray(key)

#get plaintext from input
plain = sys.stdin.buffer.read()
plain = bytearray(plain)
#declare a new bytearray
output = bytearray()

#loop both and xor. then append the bytearrays
i = 0
while(i < len(key)):
    output.append(key[i]^plain[i])
    i+=1
    
sys.stdout.buffer.write(output)
print()
