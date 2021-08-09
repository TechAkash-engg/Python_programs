f1=input("Enter the file name: ")
infile = open(f1,"r")

def Convert(string): 
    li = list(string.split(" "))
    return li

conv=[]
for ele in infile:
    conv.append(ele.strip())
print(conv)
total = 0

for ele in conv:
    sample=Convert(ele)
    print(sample)
    n=len(sample)
    total=sum(map(int,sample))
    avg=total/n
    print("Total score: ",total,"\nAverage score: ",avg)

    
