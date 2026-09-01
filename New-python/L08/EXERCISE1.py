with open('employees.txt','w')as emp_fline:
    for count in range(1, num_emps+1):
        print('enter data # ',count,sep='')
        name = input('name :')
        id_num = input('ID :')
        dept = input('Deartemnt :')
        emp_fline.write(name+'\n')
        emp_fline.write(id_num+'\n')
        emp_fline.write(dept+'\n')
        print()

    print('Employee records wrtten to employee.txt.')