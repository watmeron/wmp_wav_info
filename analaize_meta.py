#!env python3.5
import sys
import struct

infile = open(sys.argv[1], 'rb')

#data = infile.read(0x0F)

num = 0
print(infile.read(4).decode())
infile.read(4)       #読み捨て
print(infile.read(4).decode())
print(infile.read(4).decode())

size = (struct.unpack("<I",infile.read(4))[0])

#print(hex(struct.unpack("<I",infile.read(4))[0]))

print("meta size = ", size)

#infile.read(num).decode('utf-8')
#infile.read(num).decode('utf-8', 'replace')
print(infile.read(4).decode())

#Metaddata

pos = 0

while pos < size:
    tag = infile.read(4).decode()
    num = (struct.unpack("<I",infile.read(4))[0])
    pos += 8
    
    str_data = infile.read(num).decode('sjis')
    if num % 2 != 0:
        infile.read(num % 2)
        pos += num % 2
    pos += num

    #print(tag + ":" + str_data + ":" + str(pos))
    print(tag + ":" + str_data)
    
