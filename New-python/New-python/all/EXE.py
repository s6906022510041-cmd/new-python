work_hor = int(input(''))
hourly_rate = float(input(''))

if work_hor <= 40:
    pay = work_hor - 40 * hourly_rate 
print(':', format(pay, ".2f"))