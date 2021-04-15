n=int(input())
a=[int(i) for i in input().split()]
print((sum(set(a))*n-sum(a))//(n-1))
