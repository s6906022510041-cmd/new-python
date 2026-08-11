NUM_EMPLOYEES = 6

def main():
    hours =[0] *NUM_EMPLOYEES
    for index in range(NUM_EMPLOYEES):
        print('Enter the hours worked by emple=oyee',\
                index + 1,':',sep='', end='')
        hours[index] = float(input())

    pay_rate = float(input('Enter'))

    for index in range(NUM_EMPLOYEES):
        gross_pay =hours(index) *pay_rate
        print('Gross pay for meployee'.index+1,':$',\
              format(gross_pay, ',.2f'),sep='')

main