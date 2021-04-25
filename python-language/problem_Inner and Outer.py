import numpy

a=numpy.array([int(i) for i in input().split()])
b=numpy.array([int(i) for i in input().split()])
print(numpy.inner(a,b),numpy.outer(a,b),sep='\n')
