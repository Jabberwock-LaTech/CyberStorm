###########
# Jacob Pease
# 3/26/2020
# Binary Decoder
#########
from sys import stdin

def decode(binary, n):
	text = ""
	i = 0
	while (i < len(binary)):
		byte = binary[i:i+n]
		byte = int(byte, 2)
		if (byte == 9): #backspace
			text = text[:len(text)-1]
		else:
			text += chr(byte)
		i += n
		
	return text

def chal(binary):
	text = ""
	i=0
	n = 7
	while (i < len(binary)):
		byte = binary[i:i+n]
		byte = int(byte, 2)
		if (byte == 9): #backspace
			text = text[:len(text)-1]
		else:
			text += chr(byte)
		i += n
		if (n == 7):
			n=8
		elif (n ==8):
			n=7
	return text
			

####################MAIN###################
binary = stdin.read().rstrip("\n")
if (len(binary) % 7 == 0):
	text = decode(binary, 7)
	print("7-bit: ")
	print(text)
if (len(binary) % 8 == 0):
	text = decode(binary, 8)
	print("8-bit: ")
	print(text)
	
text = chal(binary)
print("Alternating 7-bit and 8-bit: ")
print(text)