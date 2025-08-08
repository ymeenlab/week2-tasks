#using random and date time module
import random
import datetime
num = random.randint(0,4)
if num == 1:
    print('Hello')
elif num == 2:
    print('Hi')
elif num == 3:
    print('Hey')
elif num == 4:
    print('Nice to meet you!')

a = datetime.datetime(2025,8,7)
print(a)
b = datetime.datetime.now()
print(b)
print(b.strftime("%A"))

