from sys import stdin, argv

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0987654321.,?!+='\":;@#$%*"
CA = ""

#get the number coresponding to any letter
def geti(letter):
    i = 0
    while(i < len(ALPHABET)):
        if(ALPHABET[i] == letter):
            return i
        i+=1

def getiCA(letter):
    i = 0
    while(i < len(CA)):
        if(CA[i] == letter):
            return i
        i+=1
    
def encrypt(plaintext):
    ciphertext = ""
    i = 0
    #repete for each letter
    while (i < len(plaintext)):
        j = 0
        isin = False
        while(j< len(ALPHABET)):
            if(ALPHABET[j] == plaintext[i]):
                isin = True
            j+=1
        if(isin):
            ciphertext += CA[geti(plaintext[i])]
        else:
            ciphertext += plaintext[i]
        i+=1
    return ciphertext

def decrypt(ciphertext):
    plaintext = ""
    i = 0
    while (i < len(ciphertext)):
        j = 0
        isin = False
        while(j < len(ALPHABET)):
            if(ALPHABET[j] == ciphertext[i]):
                isin = True
            j+=1
        if(isin):
            plaintext += ALPHABET[getiCA(ciphertext[i])]
        else:
            plaintext += ciphertext[i]
        i+=1
    return plaintext

##########################################################################################
###########################################################################################
#if they dont input correct tell them
try:
    mode = argv[1]
    key = argv[2].replace(" ", "")
except:
    print("You have to specify what the program is doing. use -e to encrept and -d to decrept. then enter you key. example: python VigCipher.py -e 'somekey'")
    exit(0)

text = stdin.read().rstrip("\n")



for i in range(len(key)):
    inCA = False
    for j in range(len(CA)):
        if(key[i] == CA[j]):
            inCA = True
            break
    if(inCA == False):
        CA += key[i]
        
for i in range(len(ALPHABET)):
    inCA = False
    for j in range(len(CA)):
        if(ALPHABET[i] == CA[j]):
            inCA = True
            break
    if(inCA == False):
        CA += ALPHABET[i]
        
#print(ALPHABET)
#print(CA)

if (mode == "-e"):
    #print(CA)
    #print(ALPHABET)
    result = encrypt(text)
elif(mode == "-d"):
    result = decrypt(text)


print result
