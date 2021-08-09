from heapq import nlargest
week1 = {'ankith': 20, 'sushmitha': 22, 'vijetha':21, 'leeladhar':17}
week2 = {'ankith': 21, 'sushmitha': 26, 'vijetha':17, 'leeladhar':19}

for key in week2: 
    if key in week1: 
        week2[key] = week2[key] + week1[key] 
    else: 
        pass
print("Total number of hours worked by each student is:")
print(week2)

top= nlargest(3,week2,key=week2.get)
print("\nTop 3 students in terms of total number of hours is:",)
print("NAME\t\tTOTAL HOURS")
for val in top:
    print(val,"\t\t",week2.get(val))
