import sys

# def pass_hash(password):
#     length = len(password)
    
#     while len(password) < 12:
#         password = '\xbb' + password
    
#     return "".join([chr(pow(0x1d, ord(c[1]) + c[0] - length, 0xfb))  for c in enumerate(password)])

# passw = pass_hash("password")

passw = bytearray(open("hashes", "rb").read())

for i in passw:
    print i

lista = []
x = 12
while x > 0:
    lista.append((29**(187+0-x))%251)
    x -= 1



j = 11
how_many = 0
while j >= 0:
    k = 0
    while k < 12:
        if (passw[j] == lista[k]):        #12
            how_many += 1
            break
        k += 1
    j -= 1

lens = 12 - how_many

indix = how_many
final = ""

 
tmp = indix
for z in range(indix,12):
    # print ord(passw[z])
    for t in range(255):
        if ((29**(t+tmp-lens)%251) == passw[z]):
            final += chr(t)
            tmp += 1


print final