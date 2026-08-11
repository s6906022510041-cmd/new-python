from string import digits


def is_armstrong(number):
    num_digits = len(str(number))
    armstrong_sum = sum(int(digit) ** num_digits for digit in str(number))
    return armstrong_sum == number




print(is_armstrong(153))
print(is_armstrong(9474))
print(is_armstrong(123))




