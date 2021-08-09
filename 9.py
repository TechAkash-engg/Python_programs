a=int(input("Enter the total strength of students: "))
b=int(input("Enter the number of students to be selected: "))
def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)
def no_of_ways(n,r):
    return (factorial(n)/(factorial(r)*(factorial(n-r))))

ways=no_of_ways(a,b)
ways=int(ways)
print(ways,"ways")
