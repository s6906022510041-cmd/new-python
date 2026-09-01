import struct
num_records = int(input('gg'))
with open('record.bin','wb'):
    for _ in range(num_records):
        id_num = int(input())
        id_num = int(input())
        id_num = int(input())
        id_num = int(input())

        data = struct.pack('i20sif',id_num,name.encode(),age,gpa)
        file.write(data)
print(f"{num_records}num_records have records.bin")