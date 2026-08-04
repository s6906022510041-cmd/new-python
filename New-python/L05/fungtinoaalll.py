#def greet():
#    print('hello')
#greet()

#def message():
#    print('Im Arthur')
#    print('king of')

#print('i haver message of you')
#message()
#print('goodbye')




#sdef main():
   # print('i have a message for you')
  #  message()
 #   print('goodbye')

#def message():
#    print('i am an arthur')
#    print('love python.')

#main()
    



#def greet(name):
#    print(f'Hello, {name}!')
 
#greet('Alice')
#greet('Alice2')
#reet('Alice3')
#greet('Alice4')





#def add(a,b):
#    return a + b

#result = add(3,5)
#print(result)








#def greet(name="World"):
#    print(f'Hello, {name}!')

#greet()

#greet('Alice')











#def sum_all(*args):
#    return sum(args)

#print(sum_all(1, 2, 3, 4, 5))  


#def sum_all(*args):
#    return sum(args)

#print(sum_all(4, 5, 6, 7))  












#def find_maximum(*args):
    #if not args:
   #     return None
  #  max_value = args[0]
 #   for num in args:
 #       if num > max_value:
 #           max_value = num
#   return max_value

#result = find_maximum(3, 5, 7, 2, 8)
#print(f"The maximum value is: {result}")







#def find_maximum(*args):
#    if not args:
#        return None
#    max_value = args[0]
#    for num in args:
#        if num > max_value:
#            max_value = num
#    return max_value

#result = find_maximum()
#print(f"The maximum value is: {result}")


















#def print_all(*args):
#    for index , age in enumerate(args):
#        print(f"Message {index + 1}: {age}")

#print_all('Python', 3.8, True, [1, 2, 3],{'key': 'value'})
















#def display_info(**kwargs):
#    for key, value in kwargs.items():
#        print(f"{key}: {value}")

#display_info(name="Alice", age=30 , city="New York")





















def calculate_area(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total_sum, average, maximum, minimum

numbers = [5 , 10, 15, 20, 25]
total, avg, max_num, min_num = calculate_area(numbers)

print(f"Total Sum: {total}")
print(f"Average: {avg}")
print(f"Maximum Value: {max_num}")    
print(f"Minimum Value: {min_num}")