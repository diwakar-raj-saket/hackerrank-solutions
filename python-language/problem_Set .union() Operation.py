n= int(input())
a=[int(i) for i in input().split()]
m= int(input())
b=[int(i) for i in input().split()]
print(len(set(a).union(set(b))))
