import numpy
A=[]
B=[]
n=int(input())
for i in range(int(n)):
    A.append([int(i) for i in input().split()])
for i in range(int(n)):
    B.append([int(i) for i in input().split()])
print(numpy.dot(numpy.array(A),numpy.array(B)))
