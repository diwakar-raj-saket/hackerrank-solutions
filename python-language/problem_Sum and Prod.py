import numpy
A=[]
a,b=input().split()
for i in range(int(a)):
    A.append([int(i) for i in input().split()])
print(numpy.prod(numpy.sum(numpy.array(A),axis=0)))
