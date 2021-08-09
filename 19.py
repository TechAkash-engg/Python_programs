n=int(input("Enter number of employees "))
class Employee:
    def __init__(self,pay,hour):
        self.pay=pay
        self.hour=hour

    def getAmount(self):
        return (self.pay*self.hour)

        
class Efficiency(Employee):   
    def __init__(self,pay,hour,e):
        self.pay=pay
        self.hour=hour
        self.e=e
                
    def Efficiency_amount(self):
        return (self.pay*self.hour*(1+self.e))
    
names=[]
c1=[]
c2=[]
a1=[]
a2=[]
for i in range(n):
    name=input("Name ")
    pays=float(input("Enter pay of the employee per hour "))
    hours=float(input("Enter hours a employee has worked "))
    eff=float(input("Enter the efficiency factor of the employee[0-1] "))
    names.append(name)
    
    op=Employee(pays,hours)
    bamt=op.getAmount()
    c1.append(bamt)  
    a1.append(bamt)
    a1.append(name)

    
    opeff=Efficiency(pays,hours,eff)
    aamt=opeff.Efficiency_amount()
    c2.append(aamt)
    a2.append(aamt)
    a2.append(name)

for ele in c1:
    mostb=max(c1)

for ele2 in c2:
    mosta=max(c2)

i=0
while i<len(a1):
    if a1[i]==mostb:
        s1=a1[i+1]
        break
    i+=1
    
j=0
while j<len(a2):
    if a2[j]==mosta:
        s2=a2[j+1]
        break
    j+=1

print(mostb)
print("Before applying efficiency factor\n$$Most paid employee of Athrv-ed$$")
print("Name: "+str(s1))
print("Amount: "+str(mostb))

print("\nAfter applying efficiency factor\n$$Most paid employee of Athrv-ed$$")
print("Name: "+str(s2))
print("Amount: "+str(mosta))
    




    
        
        
