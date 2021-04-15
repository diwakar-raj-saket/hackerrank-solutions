m=int(input())
for i  in range(m):
    a= int(input())
    c=set([int(i) for i in input().split()])
    b= int(input())
    d=set([int(i) for i in input().split()])
    if len(c.intersection(d))==len(c):
        print('True')
    else :
        print('False')
    
