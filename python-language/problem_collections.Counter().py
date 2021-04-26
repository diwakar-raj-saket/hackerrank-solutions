
import collections

n = int(input())
a = collections.Counter(map(int, input().split()))
b = int(input())

 = 0
for i in range(b):
    e, f = map(int, input().split())
    if a[e]: 
        c += f
        a[e] -= 1
print(c)
