'''t=int(input())
for i in range(t):
    g,p=map(int,input().split())
    n=int(input())
    c1=0
    c2=0
    c3=0
    c4=0
    for ele in range(n):
        a,b=map(int,input().split())
        c1=c1+a*g
        c2=c2+b*p
        c3=c3+a*p
        c4=c4+b*g
    if (c1+c2)<(c3+c4):
        print(c1+c2)
    else:
        print(c3+c4)

        

t=int(input())
a=0
b=7
for i in range(t):
    n=int(input())
    if (a-n)<(b-n):
        print("A")
        a=n
    elif (a-n)>(b-n):
        print("B")
        b=n
    else:
        if a>b:
            print("A")
            a=n
        else:
            print("B")
            b=n
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))[:n]
    k=max(a)
    m=a.index(k)
    s=sum(a)
    if k < abs(s-k):
        print("Yes")
    else:
        print("No")



t=int(input())
stack = []
arr=[]
ham=[]
def find(A):
    for i in range(len(A)):
        while stack and stack[-1] < A[i]:
            stack.pop()
        stack.append(A[i])
    while stack:
        arr.append(stack.pop())
    i=len(arr)-1
    while i>=0:
        ham.append(arr[i])
        i=i-1
    for i in ham:
        print(i,end=' ')
        
A = list(map(int,input().split()))[:t]
find(A)

list1 = ["[","{","("] 
list2 = ["]","}",")"] 

def check(myStr): 
    stack = [] 
    for i in myStr: 
        if i in list1: 
            stack.append(i) 
        elif i in list2: 
            pos = list2.index(i) 
            if ((len(stack) > 0) and (list1[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return "NO"
    if len(stack) == 0: 
        return "YES"
    else: 
        return "NO"
t=int(input())
for i in range(t):
    string1 = input()
    print(check(string1))



t=int(input())
count=0
for ele in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))[:n]
    for i in range(len(a)):
        m=min(a)
        if (m>=k):
            count=0
            break
        else:
            a[i]=a[i]+1
            count+=1
    print(count)


n,q=map(int,input().split())
a=list(map(int,input().split()))[:n]
def Average(lst): 
    total=sum(lst)
    count = len(lst)
    return total/count
arr=[]
for i in range(q):
    
    l,r=map(int,input().split())
    if r>=n:
        arr=a[l:r]
        arr.insert(0,0)
    else:
        arr=a[l:r]
        
    avg1=Average(arr)
    print(int(avg1))

n,q=map(int,input().split())
a=list(map(int,input().split()))[:n]
arr=[]
s=0
for i in a:
    s+=i
    arr.append(s)
for i in range(q):
    l, r = map(int, input().split())
    if(l-1 == 0):
        s = arr[r-1]
    else:
        s = arr[r-1] - arr[l-2]
    ans = int(s/(r-l+1))
    print(ans)


t=int(input())
for i in range(t):
    req= {"0":6, "1":2, "2":5, "3":5, "4":4, "5":5, "6":6, "7":3, "8":7, "9":6}
    n=input()
    s = sum(req[c] for c in n)
    if(s%2!=0):
        j=1
        l=7
        print(l,end='')
        for k in range(2,int(s/2)+1):
            print(j,end='')
    else:
        j=1
        for k in range(1,int(s/2)+1):
            print(j,end='')
    print()


    
t=int(input())
s=input()
if 'HH' in s:
    print("NO")
else:
    str1=''
    for i in s:
        if i=='.':
            str1=str1+'B'
        else:
            str1=str1+'H'
    print("YES")
    print(str1)

    

n = int(input())
s =input()
l = list(s)
stack = []
stack.append(l[0])
for i in range(1,len(l)):
    stack.append(l[i])
    try:
        if stack[-1]==stack[-2]:
            stack.pop()
            stack.pop()
    except:
        pass
print(len(stack))

print(''.join(stack))



n=int(input())
a=list(map(int,input().split()))[:n]
b=list(map(int,input().split()))[:n]
m=min(a)
k=len(a)
c=0
s=0
while s==0:
    s=1
    for i in range(k):
        while a[i]>m:
            if a[i]>=b[i]:
                a[i]=a[i]-b[i]
                c+=1
            else:
                print(-1)
                exit()
        if a[i]<m:
            m=a[i]
            s=0
print(c)

n=int(input())
print("*   *\n*   *")
for i in range(n):
    print("*****\n*   *\n*   *")
    

n=["A","E","I","O","U","Y"]
d=["-"]
tag=list(map(str,input()))
s1=(int(tag[0])+int(tag[1]))%2
s2=(int(tag[3])+int(tag[4]))%2
s3=(int(tag[4])+int(tag[5]))%2
s4=(int(tag[7])+int(tag[8]))%2
if (tag[6] in d) and (tag[2] not in n) and s1==0 and s2==0 and s3==0 and s4==0:
    print("valid")
else:
    print("invalid")


    

str1 =list(map(str,input().strip().split()))
res = [i for ele in str1 for i in ele]
n=int(input())
out=[]
for c in res:
    if c.isupper():
        c_unicode = ord(c)
        c_index = ord(c) - ord("A")
        new_index = (c_index + n) % 26
        new_unicode = new_index + ord("A")
        abw = chr(new_unicode)
        out.append(abw)
        
    elif c.islower():
        c_index = ord(c) - ord('a') 
        c_shifted = (c_index + n) % 26 + ord('a')
        c_new = chr(c_shifted)
        out.append(c_new)
        
    elif c.isdigit():
        c_new = (int(c) + n) % 10
        out.append(str(c_new))
    else:
        out.append(c)

for x in range(len(out)): 
    print(out[x], end='')'''


n=int(input())
a=list(map(int,input().split()))[:n]
c=[]
total=sum(a)
for i in range(len(a)):
    p=total-a[i]
    if (p%7)==0:
        c.append(a[i])
    else:
        pass

if len(c)==0:
    print(-1)
else:
    z=min(c)
    print(a.index(z))
