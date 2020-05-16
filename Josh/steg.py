# Python 2.7.16 64bit
##################################################################################################################
#  Josh Romero
#  May 8, 2020
#  Introduction to Cybersecurity
##################################################################################################################


import sys

DEBUG = False

# hands all the error cases
def error(num):
    if num == 0:
        print "You are missing the '-' in one of your arguments."
    elif num == 100:
        print "Invalid command line input arguments."
    elif num == 1:
        print "The first argument must be a 's' for store or a 'r' for retrieve"
    elif num == 2:
        print "The second argument must be a 'b' for bit mode or a 'B' for Byte mode"
    elif num == 3:
        print "The third argument must be a 'o' followed by an offset (default offset is 0)"
    elif num == 4:
        print "The fourth argument must be a 'i' followed by an interval (default interval is 1)"
    elif num == 5:
        print "The fifth argument must be a 'w' followed by the name of the wrapper file with no space between w and file name"
    elif num == 6:
        print "The sixth argument must be a 'h' followed by the name of the hidden file with no space between h and file name"
    elif num == 7:
        print "file not found in present working directory"
    exit(0)


# Handles the checking of the arguments for corrections 
def check_args():
    try:
        if sys.argv[1][0] != '-':
            error(0) 
        if sys.argv[1][1] != 's' and sys.argv[1][1] != 'r':
            error(1)
        if sys.argv[2][0] != '-':
            error(0)
        if sys.argv[2][1] != 'b' and sys.argv[2][1] != 'B':
            error(2)
        if sys.argv[3][0] != '-':
            error(0)
        if sys.argv[3][1] != 'o':
            error(3)
        if sys.argv[4][0] != '-':
            error(0)
        if sys.argv[4][1] != 'i':
            error(4)
        if sys.argv[5][0] != '-':
            error(0)
        if sys.argv[5][1] != 'w':
            error(5)
        try:
            if sys.argv[6][0] != '-':
                error(0)
            if sys.argv[6][1] != 'h':
                error(6)
        except IndexError:
            if sys.argv[1][1] == 'r':
                    pass
            else:
                error(6)
    except IndexError:
        error(100)
    

# seperates the arguments and return the results
def get_arg_info():
    sort_ret = sys.argv[1][1]                   # argument 1
    bit_byte = sys.argv[2][1]                   # argument 2
    try:
        catch = sys.argv[3][2]                  # argument 3
        offset = int(sys.argv[3][2:])
    except IndexError:
        offset = 0
    try:
        catch = sys.argv[4][2]                  # argument 4
        interval = int(sys.argv[4][2:])
    except IndexError:
        interval = 1
    try:
        catch = sys.argv[5][2]
        wrapper_file = sys.argv[5][2:]          # argument 5
    except IndexError:
        error(5)
    try:
        catch = sys.argv[6][2]                  # argument 6 if there is one
        hidden_file = sys.argv[6][2:]
    except IndexError:
        if sys.argv[1][1] == 'r':               # if there is no argument 6 then if check and makes sure it is in retrieval mode
                    hidden_file = ""
        else:
            error(6)
    return sort_ret, bit_byte, offset, interval, wrapper_file, hidden_file


# stores a hidden message in the wrapper file bytes at a time
def byte_stor_secret(hidden_file, wrapper_file, offset, interval, sentinel):
    try:                                                # open files and gets the message
        W = bytearray(open(wrapper_file, "rb").read()) 
        H = bytearray(open(hidden_file, "rb").read()) 
    except IOError:                                     # if no file can be found then error
        error(7)
    i = 0
    while i < len(H):   
        s = H[i]                            # puts the hidden message in the wrapper file
        W[offset] = H[i]
        offset += interval
        i += 1
    
    i = 0
    while i < len(sentinel):                            # puts the sentinel on the wrapper file
        W[offset] = sentinel[i]
        offset += interval
        i += 1
    
    sys.stdout.write(W)                                 # displays the results
    sys.stdout.flush()


# digs through the wrapper file looking for a hidden message bytes at a time
def byte_ret_secret(wrapper_file, offset, interval, sentinel):
    try:                                                # opens files and gets the messages
        W = bytearray(open(wrapper_file, "rb").read())   
    except IOError:                                     # error if file not found
        error(7)
    H = bytearray()

    while (offset < len(W)):
        try:                                            # if we are looking thru the entire message and never see sentinel
            b = W[offset]
        except IndexError:
            break
        if b == sentinel[5]:                                # check for the sentinel 
            if H[-1:] == sentinel[4:5]:
                if H[-2:-1] == sentinel[3:4]:
                    if H[-3:-2] == sentinel[2:3]:
                        if H[-4:-3] == sentinel[1:2]:
                            if H[-5:-4] == sentinel[0:1]:
                                break                       # found entire sentinel
        H.append(b)
        offset += interval
    H = H[0:-5]      
    sys.stdout.write(H)                                 # display the results
    sys.stdout.write("\n")
    sys.stdout.flush()


# stores a hidden message in the wrapper file bits at a time
def bit_stor_secret(hidden_file, wrapper_file, offset, interval, sentinel):
    try:                                                    # open files and get the message
        W = bytearray(open(wrapper_file, "rb").read())    
        H = bytearray(open(hidden_file, "rb").read()) 
    except IOError:                                         # error if file not found
        error(7)                    
    i = 0

    while i < len(H):                                       # change the less significant bit with the next bit in the hidden message
        for j in range(8):
            W[offset] &= 11111110
            W[offset] |= (((H[i] & 10000000) >> 7))
            H[i] = ((H[i] << 1) & (2 ** 8 -1) )
            offset += interval
        i += 1
    
    i = 0
    while i < len(sentinel):                                # change the less significant bit with the next bit in the sentinel message
        for j in range(8):
            W[offset] &= 11111110
            W[offset] |= ((sentinel[i] & 10000000) >> 7)
            sentinel[i] = ((sentinel[i] << 1) & (2 ** 8 - 1) ) 
            offset += interval    
        i += 1
    
    sys.stdout.write(W)                                     # display the results
    sys.stdout.flush()


# digs through the wrapper file looking for a hidden message bits at a time
def bit_ret_secret(wrapper_file, offset, interval, sentinel):
    try:                                                    # open file and get message
        W = bytearray(open(wrapper_file, "rb").read()) 
    except IOError:                                         # error it file not found
        error(7)   
    H = bytearray() 
    i = 0

    while offset < len(W):                                  # get the less significant bit and create the hidden message
        b = 0
        for j in range(8):
            try:                                            # if we are looking thru the entire message
                b |= (W[offset] & 00000001)
            except IndexError:
                break
            if j < 7:
                b = ((b << 1) & (2 ** 8 - 1))
                offset += interval

        if b == sentinel[5]:                                # check for the sentinel 
            if H[-1:] == sentinel[4:5]:
                if H[-2:-1] == sentinel[3:4]:
                    if H[-3:-2] == sentinel[2:3]:
                        if H[-4:-3] == sentinel[1:2]:
                            if H[-5:-4] == sentinel[0:1]:
                                break                       # found entire sentinel

        H.append(b)
        offset += interval
    H = H[0:-5]                                             # remove sentinel from the hidden message
    sys.stdout.write(H)                                     # display message
    sys.stdout.write("\n")
    sys.stdout.flush()


##################################################      Main Code       ##################################################

sentinel = bytearray([0x0, 0xff, 0x0, 0x0, 0xff, 0x0])

if DEBUG:
    sort_ret = 'r'
    bit_byte = 'B'
    offset = 1024
    interval = 1
    # wrapper_file = "stegged-bit.bmp"
    wrapper_file = "tmp3.bmp"
    # hidden_file = "hide_this.txt"
    hidden_file = ""
else:
    # checks the arguments for correctness
    check_args()
    # sets arguments to names 
    sort_ret, bit_byte, offset, interval, wrapper_file, hidden_file = get_arg_info()



# finds the correct action
if bit_byte == 'b' and sort_ret == 's':
    bit_stor_secret(hidden_file, wrapper_file, offset, interval, sentinel)
elif bit_byte == 'b' and sort_ret == 'r':
    bit_ret_secret(wrapper_file, offset, interval, sentinel)
elif bit_byte == 'B' and sort_ret == 's':
    byte_stor_secret(hidden_file, wrapper_file, offset, interval, sentinel)
else:
    byte_ret_secret(wrapper_file, offset, interval, sentinel)