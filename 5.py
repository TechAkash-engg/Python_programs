n=int(input("Enter the number of students="))
totalp=0
totalf=0
for i in range(n):
    r=input("Enter the result of student =")
    if r=="P":
        totalp+=1
    elif r=="F":
        totalf+=1
print("The number of students failed in exam is ->",totalf)
print("The number of students passed in exam is ->",totalp)
