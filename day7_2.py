'''def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2 

# If key is greater than middle element , ignore left half and search only in right half 

        if arr[mid] < key:
            low = mid + 1 

# If key is smaller than middle element, ignore right half and search only in left half 

        elif arr[mid] > key:
            high = mid - 1 
	
# If the key element itself is the middle element 
  
        else:
            print(low,high)
            return mid  

# If we reach here, then the element was not present  

    print(low,high,mid)
    return -1 

arr = [ 2,6,9,12,18,21,27,35,39,41,43]  
key = 25

# Function call  
result = binary_search(arr, key )  

if result != -1:
    print("Element is present at index", result)  
else:
    print("Element is not present in array") 

def gcd(a,b):
    if(b==0):
        return a 
    else:
        k=gcd( b, a%b)
        return k
        
w=gcd(156,23)
'''
T=list(map(str,input().split()))
P=list(map(str,input().split()))
n=18
m=3
for i in range(15):
    j=0 
    while j<m and P[j]==T[i+j]:
        j=j+1
        print(i,j)
    if j==m:
        print(i)
print(-1)
