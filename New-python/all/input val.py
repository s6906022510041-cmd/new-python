score = int(input('Enter a test score: '))
while score < 0 or score > 100:
    print('Enter: the score cannot be negative')
    print('or gtrater than 100.')
    score = int(input('Enter the corrct: '))