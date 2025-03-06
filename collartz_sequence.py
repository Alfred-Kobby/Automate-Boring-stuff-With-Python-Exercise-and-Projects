def collatz(number):
    try:
        if number % 2 == 0:
            num = number // 2
            print(str(num))
        else:
            num = 3 * number + 1
            print(str(num))
        return num
    except ZeroDivisionError:
        print('Error occurred')
        return None


user_input = 0
while True:
    print('Enter an integer! ')
    try:
        user_input = input()
        user_input = int(user_input)
    except ValueError:
        print('Input not an integer')
        continue
    result = collatz(user_input)
    if result == 1:
        break
