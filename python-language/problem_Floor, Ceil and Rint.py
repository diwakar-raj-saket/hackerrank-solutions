import numpy
numpy.set_printoptions(legacy='1.13')
a=numpy.array([float(i) for i in input().split()])
print(numpy.floor(a),numpy.ceil(a),numpy.rint(a),sep='\n')
