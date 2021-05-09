from collections import defaultdict 
n,m = map(int, input().split())
d = defaultdict(list)
for _ in range(1,n+1):
    d[input()].append(str(_))
    
for output in range(0,m): 
    a = input()
    if len(d[a]) == 0:
        print(-1)
    else:
        print(' '.join(d[a]))   

