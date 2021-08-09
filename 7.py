def binary_search(arr, x): 
    low = 0
    high = len(arr) - 1
    mid = 0
  
    while low <= high: 
  
        mid = (high + low) // 2
  
        # Check if x is present at mid 
        if arr[mid] < x: 
            low = mid + 1
  
        # If x is greater, ignore left half 
        elif arr[mid] > x: 
            high = mid - 1
  
        # If x is smaller, ignore right half
        #list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
        else:
            return mid
    
    return -1
 
n = int(input("Enter the number of element:"))
arr=list(map(int,input("Enter the elements : ").strip().split()))[:n]

x=int(input("Enter the search element:"))
result = binary_search(arr, x) 
  
if result!=-1: 
    print("Element "+ str(x) +" is present in location:",str(result+1)) 
else: 
    print("Element is not present in array") 
