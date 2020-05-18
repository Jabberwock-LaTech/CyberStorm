#########################################
# Jace Ziegler
# 5/7/2020
# Python 3
# Program 7: Steg
#########################################
from sys import stdout, argv

### handleing the input
try:
    st1 = argv[1]
    nd2 = argv[2]
    rd3 = argv[3]
except:
    stdout.write("You have to at least declare -s or -r, -b or -B and -W(filename)")
    quit(0)
try:
    th4 = argv[4]
except:
    th4 ="0"
try:
    th5 = argv[5]
except:
    th5 ="0"
try:
    th6 = argv[6]
except:
    th6 ="0"

sr = st1
bB = nd2

if(th4 == "0"):
    I = 1
    O = 0
    W = rd3
    H = "0"
elif(th5 == "0"):
    if(rd3[:2] == "-o"):
        I = 1
        O = int(rd3[2:])
        W = th4
        H = "0"
    elif(rd3[:2] == "-i"):
        I = int(rd3[2:])
        O = 0
        W = th4
        H = "0"
    elif(rd3[:2] == "-w"):
        I = 1
        O = 0
        W = rd3
        H = th5
elif(th6 == "0"):
    if(rd3[:2] == "-o" and th4[:2] == "-i"):
        O = int(rd3[2:])
        I = int(th4[2:])
        W = th5
        H = "0"
    elif(rd3[:2] == "-o" and th4[:2] == "-w"):
        O = int(rd3[2:])
        I = 1
        W = th4
        H = th5
    elif(rd3[:2] == "-i" and th4[:2] == "-w"):
        O = 0
        I = int(rd3[2:])
        W = th4
        H = th5
else:
    O = int(rd3[2:])
    I = int(th4[2:])
    W = th5
    H = th6
###
#handling misc exceptions
try:
    if(H == "0" and sr == "-s"):
        stdout.write("In store mode you have to input a hiddin file")
        quit(0)
except:
        stdout.write("Make sure you put your inputs in this order. -(sr) -(bB) -o<val> -i<val> -w<val> [-h<val>]")
        quit(0)
try:
    test = W
except:
    stdout.write("you must declare -w file")
    quit(0)

#Helper Functions
def get_bytearray(key_file):
    file = open(key_file, "r+b")
    key = file.read()
    file.close()
    key = bytearray(key)
    return key

#Varibles
SENTINEL = bytearray([0,255,0,0,255,0])
#print(SENTINEL)

#Get byte arrays
W = get_bytearray(W[2:])
if(H[:2] == "-h"):
    H = get_bytearray(H[2:])
   

#STORE MODE
if(sr == "-s"):
    #BYTE MODE
    if(bB == "-B"):
        i = 0
        while(i < len(H)):
            W[O] = H[i]
            O += I
            i+=1

        i = 0
        while(i < len(SENTINEL)):
            W[O] = SENTINEL[i]
            O += I
            i +=1
    #BIT MODE
    elif(bB == "-b"):
        i = 0
        while( i < len(H)):
            j = 0
            while(j < 8):
                W[O] = W[O] & 0b11111110
                W[O] = W[O] | ((H[i] & 0b10000000) >> 7)
                H[i] = (H[i] << 1) & (2 ** 8 -1)
                O += I
                j += 1
            i += 1

        i = 0
        while( i < len(SENTINEL)):
            j = 0
            while(j < 8):
                W[O] = W[O] & 0b11111110
                W[O] = W[O] | ((SENTINEL[i] & 0b10000000) >> 7)
                SENTINEL[i] = (SENTINEL[i] << 1) & (2 ** 8 -1)
                O += I
                j += 1
            i += 1
    #Incorrect Mode
    else:
        stdout.write("You must declare bit or byte mode. -b or -B")
        quit(0)
    #print it out
    stdout.buffer.write(W)
    

#RETREVE MODE
elif(sr == "-r"):
    index = 0
    H = bytearray()
    counter = 0
    #BYTE MODE
    if(bB == "-B"):
        while(O < len(W)):
            b = W[O]
            if(b == SENTINEL[counter]):
                counter+=1
                if(counter > 4):
                    break
            else:
                counter = 0
            H.append(b)
            index+=1
            O += I
        H = H[:index -5]
        
                
    #BIT MODE
    elif(bB == "-b"):
        while(O < len(W)):
            b = 0b0
            j = 0
            while(j < 8):
                b = b | (W[O] & 0b00000001)
                if(j < 7):
                    b = (b << 1) & (2 ** 8 -1)
                    O += I
                j+=1
            if(b == SENTINEL[counter]):
                counter+=1
                if(counter > 4):
                    break
            else:
                counter = 0
            H.append(b)
            index+=1
            O += I
        H = H[:index -5]
    
    #Incorrect Mode
    else:
         stdout.write("You must declare bit or byte mode. -b or -B")
         quit(0)
    #print it out
    stdout.buffer.write(H)

#Error catch
else:
    stdout.write("You must declare store or retrieve mode. -s or -r")
    quit(0)
