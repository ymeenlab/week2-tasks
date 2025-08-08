def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
#main code
num= int(input('enter the value:'))
result = factorial(num)#making fictorial funtion
print(f"The factorial of {num} is = {result}")

