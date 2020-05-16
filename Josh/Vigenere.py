from sys import *

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
c_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

##################################      does the encryption
def encrypt(plaintext, key):
    ciphertext = ""
    count = 0
    count2 = 0
    for j in range(len(plaintext)):
        if plaintext[j] not in alphabet and plaintext[j] not in c_alphabet and plaintext[j] != " ":  ###     Deals with punctuations
            count += 1
            ciphertext += plaintext[j] 
        else:
            if plaintext[j] == "\n" or plaintext[j] == ' ':     ###############     watchs out for NL and SP in the plaintext, keeps count of them
                count += 1   
            if key[(j - count + count2) % len(key)] == ' ':     ###############     watchs out for SP in the key, keeps count of them
                count2 += 1
            if plaintext[j] in alphabet:  
                shift = alphabet.index(key[(j - count + count2) % len(key)].lower())    ###### finds the appropriate shift for lower case letters
                ciphertext += alphabet[(alphabet.index(plaintext[j]) + shift) % 26]     ###### adds the correct letter with the shift to ciphertext
            elif plaintext[j] in c_alphabet:
                shift = c_alphabet.index(key[(j - count + count2) % len(key)].upper())  ###### finds the appropriate shift for upper case letters
                ciphertext += c_alphabet[(c_alphabet.index(plaintext[j]) + shift) % 26] ###### adds the correct letter with the shift to ciphertext
            else:
                ciphertext += plaintext[j]              #############   adds all non alphabets to the ciphertext
    return ciphertext

def decrypt(ciphertext, key):           ### mostly same as above
    plaintext = ""
    count = 0
    count2 = 0
    for j in range(len(ciphertext)):
        if ciphertext[j] not in alphabet and ciphertext[j] not in c_alphabet and ciphertext[j] != " ":  ###     Deals with punctuations
            count += 1
            plaintext += ciphertext[j] 
        else:
            if ciphertext[j] == "\n" or ciphertext[j] == ' ':
                count += 1
            if key[(j - count + count2) % len(key)] == ' ':
                count2 += 1  
            if ciphertext[j] in alphabet:
                shift = alphabet.index(key[(j - count + count2) % len(key)].lower())
                plaintext += alphabet[(alphabet.index(ciphertext[j]) - shift) % 26]         ###     subtracts the shift instead of adds it 
            elif ciphertext[j] in c_alphabet:
                shift = c_alphabet.index(key[(j - count + count2) % len(key)].upper())
                plaintext += c_alphabet[(c_alphabet.index(ciphertext[j]) - shift) % 26]     ###     subtracts the shift instead of adds it 
            else:
                plaintext += ciphertext[j] 
    return plaintext



####################################        Main Code          #################################
##################      Get the agruments
try:
    mode = argv[1]
    key = argv[2]
except:                 #################       if the user does not give arguments 
    print "This program requires two commandline arguments."
    exit(0)


# text = stdin.read().rstrip("\n")

if mode == "-e":
    ciphertext = ""
    for line in stdin:
        ciphertext += encrypt(line, key)
    print ciphertext
elif mode == "-d":
    plaintext = ""
    for line in stdin:
        plaintext += decrypt(line, key)
    print plaintext