#####################################
#Jace Ziegler
#python 3.6
#Covert storage communication decoder
#####################################
from ftplib import FTP
from sys import stdout

#decodes a 7 or 8 bit string of binary
def decode(binary, n):
	text = ""
	i = 0
	while (i< len(binary)):
		byte = binary[i:i+n]
		byte = int(byte, 2)
		if(byte == 8):
			text = text[:-1]
		else:
			text += chr(byte)
		i += n

	return text

#this is for the diffrent bit metods. supports 7 and 10
METHOD = 10 

 # globals (FTP specifics)
IP = "jeangourd.com"
PORT = 21
FOLDER = "10"

#the file/folder contents
contents = []

#connect to the FTP sever in spacific IP and Port, navigate to specifed folder, and coppy contents, then disconect
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login()
ftp.cwd(FOLDER)
ftp.dir(contents.append)
ftp.quit()

#what we will print out
text = ""
#for 10bit you need one long binary to concatinate
binary = ""

#go row by row
for row in contents:
    #7bit method
    if(METHOD == 7):
        #if first three are --- then we pay attention
        if( row[0:3] == "---"):
            #from the fourth spot to the end of permisouns we replace all - with 0 and all rwx with 1 to get a num in base 2
            byte = row[3:10].replace("-","0").replace("x",'1').replace("w",'1').replace("r",'1')
            #binary to base 10
            byte = int(byte, 2)
            #base 10 to letters
            text += chr(byte)
    #10bit method
    elif(METHOD == 10):
        #takes all pernisons and turns it into one long binary
        binary = binary + row[0:10].replace("-","0").replace("x",'1').replace("w",'1').replace("r",'1').replace("d","1")

if(METHOD == 10):
    #if 7 - bit
    if (len(binary)%7 == 0):
        text = decode(binary, 7)
        stdout.write(text)
    # if 8 bit
    if(len(binary)%8 ==0)
        text = decode(binary, 8)
        stdout.write("\n"+text)
elif(METHOD == 7):
    stdout.write(text)
