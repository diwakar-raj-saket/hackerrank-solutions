# Enter your code here. Read input from STDIN. Print output to STDOUT
n= int(input())
a=[int(i) for i in input().split()]
m= int(input())
b=[int(i) for i in input().split()]
print(len(set(a).symmetric_difference(set(b))))
