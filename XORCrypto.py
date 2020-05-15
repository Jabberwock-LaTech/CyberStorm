# Names:        James R. Henry
# Date:         05/08/2020
# Assignment:   XOR Crypto
# Version:      Python 2

from sys import stdin, stdout, argv

def xor(message):
    output = bytearray(len(message))
    for i in range(len(message)):
        output[i] = message[i] ^ key[i % len(key)]
    return output

message = bytearray(stdin.read().rstrip("\n"))

key = bytearray(open("740cfd3199e2a52a2331528145eab143", "rb").read())

cipher = xor(message)

stdout.write(cipher)