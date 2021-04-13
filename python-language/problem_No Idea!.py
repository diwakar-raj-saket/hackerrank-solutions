n,m = input().split()
s=list()
s =list(map(int, input().strip().split()))

a = set(map(int, input().strip().split()))
b = set(map(int, input().strip().split()))
h=0
for i in s:
    if i in a:
        h+=1
    if i in b:
        h-=1
print(h)
