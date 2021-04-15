n=int(input())
a=set([int(i) for i in input().split()])
m=int(input())
for i  in range(m):
    b,c= input().split()
    d=set([int(i) for i in input().split()])
    if b=="intersection_update":
        a.intersection_update(d)
    elif b=="update":
        a.update(d)
    elif b=="symmetric_difference_update":
        a.symmetric_difference_update(d)
    elif b=="difference_update":
        a.difference_update(d)
print(sum(a))
