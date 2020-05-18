from sys import stdin, argv

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0987654321.,?!+='\":;@#$%*"


#get the number coresponding to any letter
def geti(letter):
    i = 0
    while(i < len(ALPHABET)):
        if(ALPHABET[i] == letter):
            return i
        i+=1
   

def encrypt(plaintext, key):
    ciphertext = ""
    i = 0
    ikey = 0
    #repete for each letter
    while (i < len(plaintext)):
        #if letter then do the cypering
        j = 0
        isin = False
        while(j< len(ALPHABET)):
            if(ALPHABET[j] == plaintext[i]):
                isin = True
            j+=1
        if(isin):
            a = geti(plaintext[i])
            b = geti(key[ikey])
            c = (int(a) + int(b)) % 77

            add = ALPHABET[c]

            ikey += 1
            if (ikey >= len(key)):
                ikey = ikey%len(key)
        #else just put it in
        else:
            add = plaintext[i]
        
        ciphertext += add
            
        i+=1
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    i = 0
    ikey = 0
    #repete for each letter
    while (i < len(ciphertext)):
        #if letter decrypt
        j = 0
        isin = False
        while(j < len(ALPHABET)):
            if(ALPHABET[j] == ciphertext[i]):
                isin = True
            j+=1
        if(isin):  
            a = geti(ciphertext[i])
            b = geti(key[ikey])
            c = int(a) - int(b)
            if(c < 0):
                c = c + 77
            add = ALPHABET[c]


            ikey += 1
            if (ikey >= len(key)):
                ikey = ikey%len(key)
        #not letter then tack it on
        else:
            add = ciphertext[i]
        plaintext += add
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

if (mode == "-e"):
    result = encrypt(text, key)
elif(mode == "-d"):
    result = decrypt(text, key)


print result
