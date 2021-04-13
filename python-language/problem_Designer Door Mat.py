# Enter your code here. Read input from STDIN. Print output to STDOUT
x=input().split()
n=int(x[0])
m=int(x[1])

j=1
k=(m-j*3)/2
j=int(j)
k=int(k)
a='-'
b='.|.'
for i in range(int((n)/2)):
    print(a*k+b*j+a*k)
    j=j+2
    k=(m-j*3)/2
    j=int(j)
    k=int(k)
k=int((m-7)/2)
print(a*k+"WELCOME"+a*k)
j=j-2
k=(m-j*3)/2
j=int(j)
k=int(k)
for i in range(int((n+1)/2),n):
    print(a*k+b*j+a*k)
    j=j-2
    k=(m-j*3)/2
    j=int(j)
    k=int(k)


