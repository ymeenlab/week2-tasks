#creating an empty file to store 5 students name
stu=[]
#storing student's name using for loop in the correct index
for i in range(5):
    name=input("Enter the name of student: ")
    stu.append(name)
    i+=1
#printing list in reverse
for i in range(len(stu)-1,-1,-1):    
    print(stu[i])