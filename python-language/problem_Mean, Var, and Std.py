import numpy
A=[]
n,m=input().split()
for i in range(int(n)):
    A.append([int(i) for i in input().split()])
print(numpy.mean(numpy.array(A), axis = 1),numpy.var(numpy.array(A), axis = 0),round(numpy.std(numpy.array(A),axis = None),11),sep='\n')
    
