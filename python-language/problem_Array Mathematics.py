import numpy
A=[]
B=[]
n,m=input().split()
for i in range(int(n)):
    A.append([int(i) for i in input().split()])
for i in range(int(n)):
    B.append([int(i) for i in input().split()])
A=numpy.array(A)
B=numpy.array(B)
print(numpy.add(A,B),numpy.subtract(A,B),numpy.multiply(A,B),numpy.floor_divide(A,B),numpy.mod(A,B),numpy.power(A,B),sep='\n')
