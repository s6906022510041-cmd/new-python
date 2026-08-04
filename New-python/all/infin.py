keep_go ='y'
while keep_go == 'y':
    cales = float(input('enter: '))
    comm_rat = float(input('enter: '))
    commission = cales * comm_rat
    print(f'the commission is ${commission:.2f}')
    keep_go = input('do you want' + \
                    'commission (Enter y for yes): ') 
    

 