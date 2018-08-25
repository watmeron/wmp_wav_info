#!env python3.5
import sys
import struct

# Metadata dict
meta_dict = {
    "IPRD" : "album",
    "IART" : "artist",
    "INAM" : "title",
    "IGNR" : "genre",
    "ITRK" : "track"
}

infile = open(sys.argv[1], 'rb')

if "RIFF" != infile.read(4).decode():
    print("This File is not wave format.")
    exit(1)

infile.read(4)

if "WAVE" != infile.read(4).decode():
    print("This File is not wave format.")
    exit(1)

while "LIST" != infile.read(4).decode():
    pass

size = (struct.unpack("<I",infile.read(4))[0])

while "INFO" != infile.read(4).decode():
    pass


# Get Metaddata

pos = 0
str = ""

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
    if tag in meta_dict:
        str += "-metadata \"" + meta_dict[tag] + "\"=\"" + str_data[:-1].replace(' ', '　') + "\" "

print(str)
    
