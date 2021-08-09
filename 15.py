file1 = open("amount.txt", "r")
file2 = open("keys.txt", "r")

for ele in file2:
    name=ele.split()
    N=0

for ele in file1:
    names=ele.split()
    amount=0
    for i in range(len(name)):
        if name[i]==names[i]:    
            amount+=1
           
    print("Employee",N," Amount=",amount)
    N+=1
    continue
