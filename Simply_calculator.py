# Simple calculator
print("Welcome to the calculator")
repeat = True
while repeat:
    operator = None
    while operator not in ['+', '-', '*', '/']:
        operator = input("Enter an operator (+ - * /): ")
        if operator not in ['+', '-', '*', '/']:
            print('Error: You entered an invalid operator!')

    
    while True:
        try:
            number_1 = float(input("Enter the number 1: "))
            break
        except ValueError:
            print("Error: You entered the wrong number!")

    while True:
        try:
            number_2 = float(input("Enter the number 2: "))
            if operator == '/' and number_2 == 0:
                print('Error: Division by zero!')
                continue
            break
        except ValueError:
            print("Error: You entered the wrong number!")


    if operator == '+':
        print('Result is: ', number_1 + number_2)
    elif operator == '-':
        print('Result is: ', number_1 - number_2)
    elif operator == '*':
        print('Result is: ', number_1 * number_2)
    elif operator == '/':
        print('Result is: ', number_1 / number_2)

    resume = input("Do you want to continue? (Y/N): ")
    if resume.upper() != "Y":
        repeat = False

print('Thank you for using the calculator.')