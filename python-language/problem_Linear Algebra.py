import numpy as np
n=int(input())
M=[]
for i in range(n):
    M.append([float(i) for i in input().split()])
print(round(np.linalg.det(M),2))
