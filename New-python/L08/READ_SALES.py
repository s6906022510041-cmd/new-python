with open('salse.txt','r')as sales_file:
    line = sales_file.readline()
    while line !='':
        amount = float(line)
        print(float(amount, '.2f'))
        line = sales_file.readline()