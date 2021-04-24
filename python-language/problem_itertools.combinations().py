from itertools import combinations 
A=input().split()
print(*([''.join(i) for j in range(1,int(A[1])+1) for i in list(combinations(sorted(A[0]),j))]),sep='\n')
