import numpy as np
a=[int(i) for i in input().split()]
A=[]
for j in range(a[0]):
    A.append([int(i) for i in input().split()])
A=np.array(A)
print(np.transpose(A),A.flatten(),sep='\n')
