t="1110011101"
p1=0
p2=0

for i in t:
    if i == "1":
        p1+=2
    else:
        p2+=1     
total = p1+p2 
print("The total amount Rohan earned in 10 days is",total)
