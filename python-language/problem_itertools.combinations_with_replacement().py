from itertools import combinations_with_replacement as cwr
a=input().split()
print(*[''.join(i) for i in list(cwr(sorted(a[0]),int(a[1])))],sep='\n')
