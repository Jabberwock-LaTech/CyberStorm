# Names:        James R. Henry
# Date:         03/30/2020
# Assignment:   Vigenere Cipher
# Version:      Python 2

# import stdin & argv from sys
from sys import stdin, argv

# create shift table for both upper and lower case characters
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha = "abcdefghijklmnopqrstuvwxyz"

# encrypt a plaintext input using supplied key
def encrypt(plaintext, key):
    # counter
    i = 0
    # key counter
    j = 0
    # variable for the encoded text
    ciphertext = ""
    # step through the plain text
    while (i < len(plaintext)):
        # grab the current step character
        char = plaintext[i]
        # if the character is a letter
        if (char.isalpha()):
            # if the character is uppercase
            if (char.isupper()):
                # skip whitespace characters
                if (key[j % len(key)] == " "):
                    # increment key counter
                    j += 1
                # index current character from table
                c = ALPHA.find(char)
                # index appropriate key character from table
                # return to the beginning of the key if plain text
                # is longer than the key once you hit the end
                k = ALPHA.find(key[j % len(key)])
                # encode the character into the string
                ciphertext += ALPHA[(c + k) % len(ALPHA)]
                # increment key counter
                j += 1
            # if character is lowercase
            else:
                # skip whitespace characters
                if (key[j % len(key)] == " "):
                    # increment key counter
                    j += 1
                # index current character from table
                c = alpha.find(char)
                # index appropriate key character from table
                # return to the beginning of the key if plain text
                # is longer than the key once you hit the end
                k = ALPHA.find(key[j % len(key)])
                # encode the character into the string
                ciphertext += alpha[(c + k) % len(alpha)]
                # increment key counter
                j += 1
        # if the character is not a letter
        else:
            # carry over any non-letters
            ciphertext += char
        # increment counter
        i += 1
    # return encoded text
    return ciphertext

# decrpyt encrypted text using supplied key
def decrypt(ciphertext, key):
    # counter
    i = 0
    # key counter
    j = 0
    # variable for decoded text
    plaintext = ""
    # step through the encoded text
    while (i < len(ciphertext)):
        # grab the current step character
        char = ciphertext[i]
        # if the character is a letter
        if (char.isalpha()):
            # if the character is uppercase
            if (char.isupper()):
                # skip whitespace characters
                if (key[j % len(key)] == " "):
                    # increment key counter
                    j += 1
                # index the current character from the table
                c = ALPHA.find(char)
                # index appropriate key character from table
                # return to the beginning of the key if encoded text
                # is longer than the key once you hit the end
                k = ALPHA.find(key[j % len(key)])
                # decode the character into the string
                plaintext += ALPHA[(c - k + len(ALPHA)) % len(ALPHA)]
                # increment key counter
                j += 1
            else:
                if (key[j % len(key)] == " "):
                    # increment key counter
                    j += 1
                # index the current character from the table
                c = alpha.find(char)
                # index appropriate key character from table
                # return to the beginning of the key if encoded text
                # is longer than the key once you hit the end
                k = ALPHA.find(key[j % len(key)])
                # decode the character into the string
                plaintext += alpha[(c - k + len(ALPHA)) % len(ALPHA)]
                # increment key counter
                j += 1
        # if the character is not a letter
        else:
            # carry over any non-letters
            plaintext += char
        # increment counter
        i += 1
    # return decoded text
    return plaintext

# if no arguments were passed when running the program
if (len(argv) == 1):
    # request mode and key
    print "Please include mode (-e or -d) and key."
    # exit
    exit(0)
# if a mode but no key were passed when running the program
elif (len(argv) == 2):
    # request a key
    print "Please include a key."
    # exit
    exit(0)
# both a mode and key were passed
else:
    # mode = arguemnt at index 1
    mode = argv[1]
    # key = argument at index 2 & convert to uppercase
    key = argv[2].upper()
# if there is an argument at index 3
if (len(argv) == 4):
    # copy argument at index 3 to variable text
    text = argv[3]
# otherwise 
else:
    # record input from stdin to variable text
    text = stdin.read().rstrip("\n")

# if mode is -e 
if (mode == "-e"):
    # encrypt supplied text with supplied key
    # store in encoded string
    ciphertext = encrypt(text, key)
    # print encoded string
    print ciphertext
# if mode is -d
elif (mode == "-d"):
    # decode supplied text with supplied key
    # store in decoded string
    plaintext = decrypt(text, key)
    # print decoded string
    print plaintext