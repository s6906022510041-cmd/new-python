import struct
recprd = (1,'jhon doe',20,3.75)
with open('records.bin','wb')as file:
    data = struct.pack('i20sif', recprd[0],recprd[1].encode('utf-8'),recprd[2],recprd[3])
    file.write(data)