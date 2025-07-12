print('welcome to the calculator')
def calculatorFun(num1,num2,operation):
    if operation == '+':
        result = num1 + num2
        return num1, '+', num2, '=', result
    elif operation == '-':
        result = num1 - num2
        return num1, '-', num2, '=', result
    elif operation == '*':
        result = num1 * num2
        return num1, '*', num2, '=', result
    elif operation == '/':
        if num2 != 0:
            if num2 != 0:
                result = num1 / num2
                return num1, '/', num2, '=', result
            else:
                return 'Error: Division by zero is not allowed.'
    else:
        return 'Invalid operation'
           
while True:
    print('Do you want to perform another operation? (yes/no)')
    choice = input('Choice: ').lower()
    if choice == 'yes':
        print('please enter first number . ')
        num1=float(input('Number 1: '))
        print('please enter opperation you want to perform (+,-,*,/): ')
        operation=input('Operation: ')
        print('please enter second number . ')
        num2=float(input('Number 2: '))

        print(calculatorFun(num1,num2,operation))

    elif choice == 'no':
        print('Thank you for using the calculator!')
        break
    else:
        print('Invalid choice. Please enter yes or no.')        

