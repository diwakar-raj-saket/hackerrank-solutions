import itertools  
print(*list(itertools.product([int(i) for i in input().split()], [int(i) for i in input().split()])))
