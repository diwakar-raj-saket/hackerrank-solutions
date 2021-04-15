a=set([int(i) for i in input().split()])
t=int(input())
count=0
for j in range(t):
    b=set([int(i) for i in input().split()])
    if sum(b-a)!=0 and b!=a:
        print("False")
        count+=1
        break;
if(count==0):
    print('True')
