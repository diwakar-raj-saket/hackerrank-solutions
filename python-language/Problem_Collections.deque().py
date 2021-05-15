from collections import deque
n = int(input())
d=deque()
for i in range(n):
    a = input().split()
    getattr (d, a[0])(*a[1] if len(a) > 1 else [])
    
print(*d)
