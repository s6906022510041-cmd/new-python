input_string = input("Enter: ")
modified_string = ""
vowels = "aeiouAEIOU"
for char in input_string:
    upper_char = char.upper()
    if upper_char in vowels:
        nodified_sting += "*"
    else:
        modified_string += upper_char
print("modified string:",modified_string)