n=int(input("Enter the number of inputs ="))
for i in range(n):
    str1=input("Enter the string of Ravi ")
    str2=input("Enter the string of Rohan ")
    if str1.swapcase()==str2 and str1==str2.swapcase():
        print("EQUAL")
    else:
        print("NOT EQUAL")
