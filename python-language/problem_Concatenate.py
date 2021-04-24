import numpy
a=[int(i) for i in input().split()]
A=[]
for i in range(a[0]):
    A.append([int(i) for i in input().split()])
B=[]
for i in range(a[1]):
    B.append([int(i) for i in input().split()])
print(numpy.concatenate((A,B),axis=0))
