from itertools import permutations 
A=input().split()
print(*sorted([''.join(i) for i in list(permutations(A[0],int(A[1])))]),sep='\n')
