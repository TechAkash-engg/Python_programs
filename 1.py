v = int(input())#volume
c = v**(1/3) #side of cube

if (round(c) % 2) == 0:
    print('The side is even number')
else:
    print('The side is odd number')
