# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# student = [['joe'],['kim'],['sam'],['sue'],['kelly'],['chris']]

# matrix[0][1]=10
# print(matrix)


# for row in matrix :
#     for elemrnt in row:
#         print(elemrnt,end='')
# print()




import random 

ROWS = 3
COLS = 4

def main():
    values=[[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]
    
    for r in range(ROWS):
        for c in range(COLS):
            values[r][c]=random.randint(1,100)
    print(values)
main