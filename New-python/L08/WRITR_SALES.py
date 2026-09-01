num_day = int(input('For how mabny days do yoy have asles? '))
with open('sales.txt','w')as sales_file:
    for count in range(1,num_day+1):
        sales = float(input(f'Enther the sales for day #{count}: '))
        sales_file.write(str(sales)+'\n')
print('data written to sales.txt')