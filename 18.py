arr=[1,2,4,5]
n=len(arr)
print(arr)
try:
    for i in range(n+1):
        if arr[i]==2:
            try:
                raise("DataNotValid")
          
            except DataNotValid as error:
                print("Data not valid")
                break

except IndexError:
    print("Index error occured")

            
       
    
    
    
               
