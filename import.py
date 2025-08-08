#main.py
import utils
print('choose any one:')
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print('5. square')
choice = int(input("Enter your choice: "))
if choice == 1:
    print(utils.addition(5,6))
if choice == 2:
    print(utils.subtraction(40,23))
if choice == 3:
    print(utils.multiplication(23,40))    
if choice == 4:
    print(utils.division(4,2))
if choice == 5:
    print(utils.square(5))

