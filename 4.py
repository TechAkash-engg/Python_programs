n= int(input("Enter the value of 'n': "))  
def Fibunacci(x):  
   if x <= 1:  
       return x 
   else:  
       return(Fibunacci(x-1) + Fibunacci(x-2))
if n<0:
    print("Enter the positive integer")
    n= int(input("Enter the value of 'n': "))
else:
    print("Fibonacci series:")
    for i in range(n):
        print(Fibunacci(i),end=' ')
