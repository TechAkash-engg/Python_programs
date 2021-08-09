d= str(input("Enter the data:\n"))#n
da = d.split()#m
s = str(input("Enter subject to find:\n"))#p

counter=d.count(s)
res=[i for i in range(len(d)) if d.startswith(s,i)]

count = 0
no = 0

for i in da:
    no += 1
    if s in i:
        wo = str(no)
        if wo=="1":
            wo = wo +"st"
        elif wo=="2":
            wo = wo +"nd"
        elif wo=="3":
            wo = wo +"rd"
        else:
            wo = wo +"th"           
        toc = i.index(s)+1
        loc = str(toc)
        if loc=="1":
            loc = loc +"st"
        elif loc=="2":
            loc = loc +"nd"
        elif loc=="3":
            loc = loc +"rd"
        else:
            loc = loc +"th"
        if len(da)>1:
            print("Subject",s,"was found in",wo,"word and the",loc,"location of",wo,"word")
            count += 1            
    else:
        continue
if len(da)>1:
    print("Number of times subject",s,"appeared in the data given is",count)
else:
    for i in res:
        if i=="0":
            i=i+1+str("st")
        elif i==1:
            i=i+1+str("nd")
            
        print("Subject",s,"was found in",wo,"word and the",str(i),"location of",wo,"word")
    print("Number of times subject",s,"appeared in the data given is",counter)
