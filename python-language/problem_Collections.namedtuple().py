from collections import namedtuple
n =  int(input())
sun = 0 
sheet = namedtuple("sheet",input().split() )
for i in range(n):
    sun += int(sheet(*input().split()).MARKS)   
    
print(sun/n)
