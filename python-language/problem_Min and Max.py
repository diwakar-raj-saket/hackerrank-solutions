import numpy
A=[]
n,m=input().split()
for i in range(int(n)):
    A.append([int(i) for i in input().split()])
print(numpy.max(numpy.min(numpy.array(A), axis = 1)))
