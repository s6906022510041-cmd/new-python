#count = 0 
#while count < 5:
#    print('hello : ',count)
#    count += 1



import random
print('What is my magic number (1 to 100)?')
mynumber = random.randint(1,100)
ntrise = 1
yourguess = -1
while ntrise < 7 and yourguess != mynumber:
    msg = str(ntrise) + ">>"
    if (ntrise==6):
        print ('you last');
    yourguess = int(input(msg))
    if yourguess > mynumber: 
        print('--> to high')
    else :
        print('--> to low')
    ntrise += 1

    if yourguess == mynumber :
        print("yes in's",mynumber)
    else:
        print("Sorry my number is",mynumber)