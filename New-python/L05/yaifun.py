
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