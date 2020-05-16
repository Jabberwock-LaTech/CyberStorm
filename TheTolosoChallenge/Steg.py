# Names:        James R. Henry
# Date:         05/08/2020
# Assignment:   Steg
# Version:      Python 2

from sys import stdin, stdout, argv

# Stop value
SENTINEL = bytearray([0, 255, 0, 0, 255, 0])
# Defaults for offset and interval
offset = 0
interval = 1

# Method to encrypt a message
def encrypt(bMode, W, H, offset, interval):
    # Wrapper File to store the message in
    envelope = W
    # Hidden File to be stored in the wrapper
    message = H

    # If mode is bit
    if (bMode == 0):
        # Counter
        i = 0
        
        # While the counter is less than the length of the message
        while (i < len(message)):

            # For each bit in the current byte
            for j in range(8):

                # Zero the last bit of the current byte of the wrapper
                envelope[offset] &= 11111110
                # Store the current bit of the message in the last
                #   bit of the current byte of the wrapper
                envelope[offset] |= ((message[i] & 10000000) >> 7)
                # Get the next bit of the current byte of the message
                message[i] = (message[i] << 1) & (2 ** 8 - 1)
                # Increment the offset by the Interval
                offset += interval

            # Increment counter
            i += 1

        # Reset counter
        i = 0

        # While counter is less than the length of the stop value
        while (i < len(SENTINEL)):

            # For each bit in the current byte of the stop value
            for j in range(8):

                # Zero the last bit of the current byte
                envelope[offset] &= 11111110
                # Shift the first bit of the current sentinel byte to LSB
                #   store in the bit that was just zeroed
                envelope[offset] |= ((SENTINEL[i] & 10000000) >> 7)
                # Move the next bit into place
                SENTINEL[i] = (SENTINEL[i] << 1) & (2 ** 8 - 1)
                # Increment the Offest by the Interval
                offset += interval

            i += 1

    # Else if mode is byte
    elif (bMode == 1):
        # Counter
        i = 0

        # While counter is less than the length of the message
        while (i < len(message)):

            # Replace the current byte of the wrapper with
            #   the current byte of the hidden message
            envelope[offset] = message[i]
            # Increment the Offset by the Interval
            offset += interval
            # Increment counter
            i += 1

        # Reset counter
        i = 0

        # While counter is less than the length of the sentinel value
        while (i < len(SENTINEL)):

            # Replace the current byte of the wrapper with
            #   the currenty byte of the sentinel value
            envelope[offset] = SENTINEL[i]
            # Increment the Offest by the Interval
            offset += interval
            # Increment the counter
            i += 1

# Method to decrypt a hidden message
def decrypt(bMode, W, offset, interval):
    # Wrapper file containing hidden message
    envelope = W
    # Variable to store the hidden message
    message = bytearray()

    # If mode is bit
    if (bMode == 0):

        # While the offset is less than length of the wrapper
        while (offset < len(envelope)):
            # Variable to store the bits being extracted
            bit = 0
            # Counter
            i = 0

            # Step through each bit of the current byte
            for j in range(8):
                if (offset >= len(envelope)):
                    exit(0)
                # Get the LSB of the current byte
                bit |= (envelope[offset] & 0b00000001)

                # If still getting the current byte
                if (j < 7):
                    # Shift the bit(s) to the left
                    bit = (bit << 1) & (2 ** 8 - 1)
                    # Increment the Offset by the Interval
                    offset += interval
            
            # If the bit equals the current sentinel value
            if (bit == SENTINEL[i]):
                # Variable to track exit strategy
                test = True
                # Increment counter
                i = 1
                # Variable so offest is not incorrect incase
                #   exit strategy not completed
                k = offset + interval

                # While counter less than length of the sentinel value
                while (i < len(SENTINEL)):
                    # Variable to store the bits being extracted without
                    #  loosing 'bit' incase exit strategy not completed
                    nextBit = 0

                    # Step the each bit of the current byte
                    for j in range(8):                        
                        # Get the LSB of the current byte
                        nextBit |= (envelope[k] & 0b00000001)

                        # If still getting the current byte
                        if (j < 7):
                            # Shift the bit(s) to the left
                            nextBit = (nextBit << 1) & (2 ** 8 - 1)
                            # Increment k by the Interval
                            k += interval
                    
                    # If nextBit equals current sentinel value
                    if (nextBit == SENTINEL[i]):
                        # Increment counter
                        i += 1
                        # Increment k by the Interval
                        k += interval
                    
                    # Otherwise
                    else:
                        # Set counter to 1 more than length of sentinel to exit 
                        i = len(SENTINEL) + 1 
                        # Set tracker to false
                        test = False

                # If tracker is true
                if (test):
                    # return the hidden message
                    return message
                
                # Otherwise
                else:
                    # Add bit to the message
                    message.append(bit)
                    # Increment the Offest by the Interval
                    offset += interval

            # Otherwise
            else:
                # Add bit to the message
                message.append(bit)
                # Increment the Offset by the Interval
                offset += interval

        # No sequence of bytes matched the sentinel value
        print ("Did not see Sentinel values.")
        # Quit
        exit(0)

    # Else if mode is byte
    elif (bMode == 1):

        # While offset is less than the length of the wrapper
        while (offset < len(envelope)):
            # counter
            i = 0
            # Get the current byte of the wrapper
            byte = envelope[offset]

            # If byte equals the current byte of the sentinel value
            if (byte == SENTINEL[i]):
                # Set tracker to true
                test = True
                # Increment counter
                i = 1

                # While counter is less than length of the sentinel
                while (i < len(SENTINEL)):
                    # Get the next byte of the wrapper
                    nextByte = envelope[offset + (interval * i)]

                    # If nextByte equals the current sentinel value
                    if (nextByte == SENTINEL[i]):
                        # Increment counter
                        i += 1

                    # Otherwise
                    else:
                        # Set counter to one more than the length of the sentinel
                        i = len(SENTINEL) + 1
                        # Set tracker to false
                        test = False

                # If tracker is true
                if (test):
                    # Return the hidden message
                    return message

                # Otherwise
                else:
                    # Add the last byte to the message
                    message.append(byte)
                    # Increment the Offset by the Interval
                    offset += interval
            else:
                # Add the last byte to the message
                message.append(byte)
                # Increment the Offset by the Interval
                offset += interval

        # No sequence of bytes matched the sentinel value
        print ("Did not see Sentinel values.")
        # Quit
        exit(0)

# Check proper usage, at least 3 arguments are needed
if (len(argv) < 4):
    print "At least 3 arguments required."
    print "Usage is:  python Steg.py -(sr) -(bB) -o<val> [-i<val>] -w<val> [-h<val>]"
    exit(0)
# 1st Argument must be '-s' or '-r'
elif ((argv[1] != '-s') & (argv[1] != '-r')):
    print "Mode of -s or -r required."
    print "Usage is:  python Steg.py -(sr) -(bB) -o<val> [-i<val>] -w<val> [-h<val>]"
    exit(0)
# 2nd Argument must be '-b' or '-B'
elif ((argv[2] != '-b') & (argv[2] != '-B')):
    print "Mode of -b or -B required."
    print "Usage is:  python Steg.py -(sr) -(bB) -o<val> [-i<val>] -w<val> [-h<val>]"
    exit(0)
# If mode is retrieve last argument must be wrapper
if ((argv[1] == '-r') & (argv[-1][:2] != '-w')):
    print "Retrieving, Wrapper required."
    print "Usage is:  python Steg.py -(sr) -(bB) -o<val> [-i<val>] -w<val> [-h<val>]"
    exit(0)
# If mode is store last 2 arguments must be wrapper
# and hidden respectively
if ((argv[1] == '-s') & ((argv[-2][:2] != '-w') | (argv[-1][:2] != '-h'))):
    print "Storing, Wrapper and Hidden required."
    print "Usage is:  python Steg.py -(sr) -(bB) -o<val> [-i<val>] -w<val> [-h<val>]"
    exit(0)

# Get mode from 1st argument
if (argv[1] == '-s'):
    mode = 0
elif (argv[1] == '-r'):
    mode = 1

# Get bMode from 2nds argument
if (argv[2] == '-b'):
    bMode = 0
elif (argv[2] == '-B'):
    bMode = 1

# If mode is store
if (mode == 0):
    # If all arguments are present, parse
    if (len(argv) == 7):
        offset = int(argv[3][2:])
        interval = int(argv[4][2:])
        wrapper = bytearray(open(argv[-2][2:], "rb").read())
        hidden = bytearray(open(argv[-1][2:], "rb").read())
    # If 1 argument is missing, parse
    elif (len(argv) == 6):
        if (argv[3][:2] == '-o'):
            offset = int(argv[3][2:])
            wrapper = bytearray(open(argv[-2][2:], "rb").read())
            hidden = bytearray(open(argv[-1][2:], "rb").read())
        elif (argv[3][:2] == '-i'):
            interval = int(argv[4][2:])
            wrapper = bytearray(open(argv[-2][2:], "rb").read())
            hidden = bytearray(open(argv[-1][2:], "rb").read())
    # If minimum arguments, parse
    else:
        wrapper = bytearray(open(argv[-2][2:], "rb").read())
        hidden = bytearray(open(argv[-1][2:], "rb").read())
    # Encrypt the hidden file into the wrapper
    encrypt(wrapper, hidden, offset, interval)

# If mode is retrieve
elif (mode == 1):
    # If all arguments are present, parse
    if (len(argv) == 6):
        offset = int(argv[3][2:])
        interval = int(argv[4][2:])
        wrapper = bytearray(open(argv[-1][2:], "rb").read())
    # If 1 argument is missing, parse
    elif (len(argv) == 5):
        if (argv[3][:2] == '-o'):
            offset = int(argv[3][2:])
            wrapper = bytearray(open(argv[-1][2:], "rb").read())
        elif (argv[3][:2] == '-i'):
            interval = int(argv[3][2:])
            wrapper = bytearray(open(argv[-1][2:], "rb").read())
    # If minimum arguments, parse
    else:
        #binFile = open(argv[-1][2:], "rb")
        wrapper = bytearray(open(argv[-1][2:], "rb").read())
    # Decrypt the hidden file from the wrapper
    hidden = decrypt(bMode, wrapper, offset, interval)
    stdout.write(hidden)
    stdout.flush()