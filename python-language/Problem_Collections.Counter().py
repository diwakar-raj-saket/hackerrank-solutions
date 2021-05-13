from collections import Counter

x = int(input())
shoes = list(map(int,input().split()))
shoel = Counter(shoes)
n = int(input())
sums= 0
for _ in range(n):
    skey,svalue = map(int, input().split())
    if shoel[skey]:
       sums+=svalue
       shoel[skey]-=1 
print(sums)           
