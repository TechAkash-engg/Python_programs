'''n=6
for i in range(1,n):
    if i!=5:
        k=str(i)
        print(k*i)
    else:
        k=str(i+1)
        print(k*i)
       

list1=[9,11,12,14,16,17,19,21]
a=[]
k=0
for i in list1:
    for j in range(2,i):
        if i%j==0:
            k=1
    if k==0:
        a.append(i)
    k=0
print(a)


s=input()
s=s.lower()
v=['a','e','i','o','u']
for ele in s:
    if ele not in v:
        s=s.replace(ele, '')
print(s[::-1])


n=5
m=5
for i in range(m,0,-1):
    for j in range(i):
        print(n*2,end=' ')
    n=n-1
    print(" ")

 
word=input()
word1=''
for i in word:    
    if i==',':
        word1=word1+'.'
    elif i=='.':
        word1=word1+','
    else:
        word1=word1+i
print(word1)
          

li=[1,1,0,1,1,1,0,1,1,1,1,1,1,0,1,1]
k=0
m=0
for i in li:
    if i==1:
        k+=1
    if i==0:
        k=0
    m=max(k,m)
print(m)
 
k=7
m=10
for i in range(7,2,-1):
    for j in range(m):
        print(k,end=' ')
    k=k-1
    m-=2
    print(' ')

li1=[]
li=["aba", "hey", "athrved,", "malayalam", "mam", "anusha", "Vigensh","nidhi", "Shamitha", "Sahana", "Are learning python" ]
for i in li:
    if i==i[::-1]:
        pass
    else:
        li1.append(i)
print(li1)


n=input()
n=n.lower()
v=['a','e','i','o','u']
for ele in n:
    if ele in v:
        n=n.replace(ele, '')
print(n)

'''
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a,b):
    return (a / gcd(a,b))* b

a = 15
b = 20
print('LCM of', a, 'and', b, 'is', lcm(a, b))
 