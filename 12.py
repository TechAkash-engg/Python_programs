lis = []
count = int(input('Enter the number of elements:'))
for i in range(count):
    number = int(input("Enter the element " + str(i + 1) + " :"))
    lis.append(number)

def minimum(lis, n): 

    minpos = lis.index(min(lis))       
    print("Index of smallest element is : ", minpos + 1)
    
minimum(lis, len(lis)) 
