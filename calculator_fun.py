#making a calculator function

def calculator(a,b):
    print('choose any one:')
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        result= a + b
        print(f'The final result of addition is:', result)
    elif choice == 2:
        result= a - b
        print(f'The final result of subtraction is:', result)
    elif choice == 3:
        result= a * b
        print(f'The final result of multiplication is:', result)
    elif choice == 4:
        if b != 0:
            result= a / b
            print(f'The final result of divisionis:', result)
        else:
            return "Error! Division by zero is not allowed."
    else:
        return "Invalid choice. Please choose a valid operation."
    
#main code
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
calculator(num1,num2)

