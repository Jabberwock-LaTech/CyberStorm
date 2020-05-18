def encrypt(text,s):
	result = ""
	# transverse the plain text
	for i in range(len(text)):
		char = text[i]
		# Encrypt uppercase characters in plain text
		if (char.isupper()):
			result += chr((ord(char) + s-65) % 26 + 65)
			# Encrypt lowercase characters in plain text
		else:
			result += chr((ord(char) + s - 97) % 26 + 97)
	return result
#check the above function
text = "GbqshgnabjqvwpyPjyymuXolmfqJrfizgbqlhaezrrfbrbbqDoqawOchrluarvyrbodahdyz"
s = 0

print("Plain Text : " + text)
while(s < 27):
	print("Cipher Shift {}: ".format(str(s)) + encrypt(text,s))
	s += 1