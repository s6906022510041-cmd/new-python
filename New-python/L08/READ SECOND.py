import struct
recod_format = 'i20sif'
recod_size = struct.calcsize(recod_format)
with open('records.bin','rb')as file:
    file.see;(recod_size)
    data = file.read(recod_size)
    recod = struct.unpack(record_form,data)
    recod = (recod[0],recod[1].strip('\x00'),recod[2], recod[3])
print(f'{recod[0]},{recod[1]},{recod[2]},{recod[3]}')